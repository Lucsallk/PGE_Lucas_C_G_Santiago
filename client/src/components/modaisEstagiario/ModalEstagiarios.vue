<script setup>
import { onMounted, onBeforeMount, ref } from "vue";
import { getAPI } from "../../assets/axios";
const nomeCompleto = ref("");
const cpf = ref("");
const dataDeNascimento = ref("");
const cursoDeGraduacao = ref("");
const instEnsino = ref("");
const cargaHoraria = ref(0);
const setorAlocado = ref();

const validate = (cpf) => {
  let sum = 0;
  let remainder;

  cpf = cpf.replace(".", "").replace(".", "").replace("-", "").trim();
  let allEqual = true;

  for (let i = 0; i < cpf.length - 1; i++) {
    if (cpf[i] != cpf[i + 1]) allEqual = false;
  }

  if (allEqual) return false;

  for (let i = 1; i <= 9; i++) {
    sum = sum + parseInt(cpf.substring(i - 1, i)) * (11 - i);
    remainder = (sum * 10) % 11;
  }

  if (remainder == 10 || remainder == 11) remainder = 0;
  if (remainder != parseInt(cpf.substring(9, 10))) return false;

  sum = 0;
  for (let i = 1; i <= 10; i++) {
    sum = sum + parseInt(cpf.substring(i - 1, i)) * (12 - i);
    remainder = (sum * 10) % 11;
  }

  if (remainder == 10 || remainder == 11) remainder = 0;
  if (remainder != parseInt(cpf.substring(10, 11))) return false;

  return true;
};

const adicionarEstagiario = () => {
  if (
    nomeCompleto.value === "" ||
    cpf.value === "" ||
    dataDeNascimento.value === "" ||
    cursoDeGraduacao.value === "" ||
    instEnsino.value === "" ||
    cargaHoraria.value === "" ||
    setorAlocado.value === 0
  )
    return alert("Preencha todos os campos");

  if (!validate(cpf.value)) return alert("CPF não válido");

  getAPI
    .post("/estagiarios/", {
      nomeCompleto: nomeCompleto.value,
      cpf: cpf.value,
      dataNascimento: dataDeNascimento.value,
      cursoGrad: cursoDeGraduacao.value,
      instEnsino: instEnsino.value,
      cargaHoraria: cargaHoraria.value,
      setorAlocado: setorAlocado.value,
    })
    .then(() => {
      location.reload();
    })
    .catch((err) => console.log(err));
};

const setores = ref([]);

const listarSetores = () => {
  getAPI
    .get("/setores/")
    .then((response) => {
      setores.value = response.data;
    })
    .catch((err) => console.log(err));
};

onMounted(listarSetores);
</script>
<template>
  <div
    class="modal fade"
    id="cadModal"
    tabindex="-1"
    aria-labelledby="cadModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="cadModalLabel">
            Adicionar Estagiário
          </h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
            required
          ></button>
        </div>

        <div class="modal-body">
          <div class="row">
            <div class="mb-3">
              <label for="nomeCompleto" class="form-label">Nome completo</label>
              <input
                v-model="nomeCompleto"
                id="nomeCompleto"
                class="form-control"
                placeholder="Fulado da Silva"
                type="text"
                required
              />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-6">
              <label for="cpf" class="form-label">CPF</label>
              <input
                v-model="cpf"
                id="cpf"
                class="form-control"
                placeholder="Não utilize . e -"
                type="text"
                required
              />
            </div>

            <div class="col-6">
              <label for="dataDeNascimento" class="form-label"
                >Data de nascimento</label
              >
              <input
                v-model="dataDeNascimento"
                id="dataDeNascimento"
                class="form-control"
                placeholder="Fulado da Silva"
                type="date"
                required
              />
            </div>
          </div>

          <div class="row mb-3">
            <div class="col-8">
              <div class="">
                <label for="setorAlocado" class="form-label"
                  >Setor interno da <span class="fw-semibold">PGE</span></label
                >
                <select
                  v-model="setorAlocado"
                  id="setorAlocado"
                  class="form-select"
                  required
                >
                  <option
                    v-for="setor in setores"
                    :key="setor.id"
                    :value="setor.id"
                  >
                    {{ setor.nome }}
                  </option>
                </select>
              </div>
            </div>
          </div>

          <div class="row mb-3">
            <div class="col-8">
              <label for="cursoDeGraduacao" class="form-label"
                >Curso de graduação</label
              >

              <input
                v-model="cursoDeGraduacao"
                id="cursoDeGraduacao"
                class="form-control"
                placeholder="Insira apenas uma graduação"
                type="text"
                required
              />
            </div>

            <div class="col-4">
              <label for="cargaHoraria" class="form-label">Carga horária</label>
              <input
                v-model="cargaHoraria"
                id="cargaHoraria"
                class="form-control"
                type="number"
                required
              />
            </div>
          </div>
          <div class="row">
            <div class="mb-3">
              <label for="instEnsino" class="form-label"
                >Instituição de ensino</label
              >
              <select
                v-model="instEnsino"
                class="form-select"
                id="instEnsino"
                required
              >
                <option value="Universidade Federal de Sergipe - UFS">
                  Universidade Federal de Sergipe - UFS
                </option>
                <option value="Universidade Tiradentes - UNIT">
                  Universidade Tiradentes - UNIT
                </option>
                <option value="Universidade Estacio de Sá - ESTACIO">
                  Universidade Estacio de Sá - ESTACIO
                </option>
                <option value="Faculdade Mauricio de Nassau - UNINASSAU">
                  Faculdade Mauricio de Nassau - UNINASSAU
                </option>
              </select>
            </div>
          </div>
        </div>

        <div class="modal-footer justify-content-center">
          <button
            type="button"
            class="btn btn-danger fw-semibold"
            data-bs-dismiss="modal"
          >
            Cancelar
          </button>
          <button
            @click="adicionarEstagiario"
            type="button"
            class="btn btn-success fw-semibold"
          >
            Confirmar
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
