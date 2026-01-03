from datetime import datetime
from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4

from workout_api.atleta.schemas import AtletaIn, AtletaOut, AtletaUpdate, AtletaInfor
from workout_api.atleta.models import AtletaModel
from workout_api.categorias.models import CategoriaModel
from workout_api.centro_treinamento.models import CentroTreinamentoModel

from fastapi_pagination import Page, paginate, add_pagination, LimitOffsetPage
from workout_api.contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select

router = APIRouter(prefix="/atleta", tags=["atletas"])


@router.post(
    "/",
    summary="Criar um novo atleta",
    status_code=status.HTTP_201_CREATED,
    response_model=AtletaOut,
)
async def criar_atleta(
    nome: str,
    cpf: str,
    db_session: DatabaseDependency,
    atleta_in: AtletaIn = Body(...),
):
    categoria_nome = atleta_in.categoria.name
    centro_treinamento_nome = atleta_in.centro_treinamento.nome
    categoria = (
        (
            await db_session.execute(
                select(CategoriaModel).filter_by(name=categoria_nome)
            )
        )
        .scalars()
        .first()
    )

    # Verifica se já existe o mesmo CPF cadastrado
    ## 1 - Buscar no banco o cpf
    cpf_banco = (
        (await db_session.execute(select(AtletaModel).filter_by(cpf=cpf)))
        .scalars()
        .first()
    )

    if cpf == cpf_banco.cpf:
        print("teste")
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER, detail="Já existe cpf cadastrado!"
        )

    # Essas verificações podem ser colocadas em outro lugar(atribuir essa resposabilidade a outra 'entidade' do sistema
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"A categoria {categoria_nome} não foi encontrada.",
        )

    centro_treinamento = (
        (
            await db_session.execute(
                select(CentroTreinamentoModel).filter_by(nome=centro_treinamento_nome)
            )
        )
        .scalars()
        .first()
    )

    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"O centro de treinamento {centro_treinamento_nome} não foi encontrado.",
        )
    try:
        atleta_out = AtletaOut(
            id=uuid4(), created_at=datetime.utcnow(), **atleta_in.model_dump()
        )
        atleta_model = AtletaModel(
            **atleta_out.model_dump(exclude={"categoria", "centro_treinamento"})
        )

        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_treinamento_id = centro_treinamento.pk_id

        db_session.add(atleta_model)
        await db_session.commit()

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ocorreu um erro ao inserir os dados no banco",
        )

    return atleta_out


@router.get(
    "/",
    summary="Consultar todos os Atletas",
    status_code=status.HTTP_200_OK,
    response_model=LimitOffsetPage[AtletaInfor],
)
async def todos_atletas(db_session: DatabaseDependency):
    atletas = (await db_session.execute(select(AtletaModel))).scalars().all()

    atleta_out: list[AtletaInfor] = []

    for atleta in atletas:
        atleta_out.append(AtletaInfor.model_validate(atleta))

    return paginate(atleta_out)


@router.get(
    "/{id}",
    summary="Consultar um atleta",
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def consultar_atleta(id: UUID4, db_session: DatabaseDependency) -> AtletaOut:
    atleta: AtletaOut = (
        (await db_session.execute(select(AtletaModel).filter_by(id=id)))
        .scalars()
        .first()
    )

    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"O atleta não foi encontrado pelo ID({id})",
        )

    return atleta


@router.patch(
    "/{id}",
    summary="Editar um atleta pelo seu ID",
    status_code=status.HTTP_200_OK,
    response_model=AtletaUpdate,
)
async def atualizar_atleta(
    id: UUID4, db_session: DatabaseDependency, atleta_up: AtletaUpdate = Body(...)
):
    atleta: AtletaOut = (
        (await db_session.execute(select(AtletaModel).filter_by(id=id)))
        .scalars()
        .first()
    )

    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            details=f"Não foi possível encontrar o atleta pelo ID({id})",
        )

    # Atualizar o usuário
    atleta_update = atleta_up.model_dump(exclude_unset=True)

    for key, value in atleta_update.items():
        setattr(atleta, key, value)

    await db_session.commit()
    await db_session.refresh(atleta)
    return atleta


@router.delete(
    "/{id}",
    summary="Deletar um atleta pelo ID",
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def deletar_atleta(id: UUID4, db_session: DatabaseDependency) -> AtletaOut:
    atleta: AtletaOut = (
        (await db_session.execute(select(AtletaModel).filter_by(id=id)))
        .scalars()
        .first()
    )

    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"O atleta não foi encontrado pelo ID({id})",
        )

    await db_session.delete(atleta)
    await db_session.commit()


add_pagination(router)
