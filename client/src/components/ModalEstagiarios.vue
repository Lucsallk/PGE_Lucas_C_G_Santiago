<script setup>
import { ref } from "vue";
import { getAPI } from "../assets/axios";
const nomeCompleto = ref("");
const cpf = ref("");
const dataDeNascimento = ref("");
const cursoDeGraduacao = ref("");
const instEnsino = ref("");
const cargaHoraria = ref(0);
const setorAlocado = ref();

const adicionarEstagiario = () => {
    console.log(nomeCompleto.value)
    getAPI.post("/estagiarios/", {
        nomeCompleto: nomeCompleto.value,
        cpf: cpf.value,
        dataNascimento: dataDeNascimento.value,
        cursoGrad: cursoDeGraduacao.value,
        instEnsino: instEnsino.value,
        cargaHoraria: cargaHoraria.value,
        setorAlocado: setorAlocado.value,
    }).then(response => {
        console.log(response)
        location.reload();
    }).catch(err => console.log(err))
}
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
                  class="form-select"
                  id="setorAlocado"
                >
                  <option value="1">CODIN</option>
                  <option value="2">
                    Teclonogia de informação - TI
                  </option>
                  <option value="3">
                    Recursos Humanos - RH
                  </option>
                  <option value="4">Almoxarifado</option>
                  <option value="5">Diretoria</option>
                </select>
              </div>
            </div>
          </div>

          <div class="row mb-3">
            <div class="col-8">
              <label for="cursoDeGraduacao" class="form-label"
                >Curso de graduacao</label
              >
              <input
                v-model="cursoDeGraduacao"
                id="cursoDeGraduacao"
                class="form-control"
                placeholder="Insira apenas uma graduação"
                type="text"
              />
            </div>

            <div class="col-4">
              <label for="cargaHoraria" class="form-label">Carga horária</label>
              <input
                v-model="cargaHoraria"
                id="cargaHoraria"
                class="form-control"
                type="number"
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
              >
                <option value="Universidade Federal de Sergipe - UFS">Universidade Federal de Sergipe - UFS</option>
                <option value="Universidade Tiradentes - UNIT">
                  Universidade Tiradentes - UNIT
                </option>
                <option value="Universidade Estacio de Sá - ESTACIO">
                  Universidade Estacio de Sá - ESTACIO
                </option>
                <option value="Faculdade Mauricio de Nassau - UNINASSAU">Faculdade Mauricio de Nassau - UNINASSAU</option>
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
            Save changes
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
