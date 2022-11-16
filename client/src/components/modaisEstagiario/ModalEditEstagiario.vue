<script setup>
import { getAPI } from '../../assets/axios';
const props = defineProps(["dadosEstagiario"]);

const editarEstagiario = (dadosEstagiario) => {
  console.log(dadosEstagiario.id);
  console.log(dadosEstagiario.nomeCompleto);
  console.log("/estagiarios/" + dadosEstagiario.id + "/")
  getAPI.patch("/estagiarios/" + dadosEstagiario.id + "/", {
        id: dadosEstagiario.id,
        nomeCompleto: dadosEstagiario.nomeCompleto,
        cpf: dadosEstagiario.cpf,
        dataNascimento: dadosEstagiario.dataDeNascimento,
        cursoGrad: dadosEstagiario.cursoDeGraduacao,
        instEnsino: dadosEstagiario.instEnsino,
        cargaHoraria: dadosEstagiario.cargaHoraria,
        setorAlocado: dadosEstagiario.setorAlocado,
    }).then(response => {
        console.log(response)
        location.reload();
    }).catch(err => console.log(err))
};

</script>

<template>
  <div
    class="modal fade"
    id="editModal"
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
              <label for="nomeCompleto" class="form-label"
                >Nome completo:</label
              >
              <input
                v-model="props.dadosEstagiario.nomeCompleto"
                id="nomeCompleto"
                class="form-control"
                placeholder="Fulado da Silva"
                type="text"
              />
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
            @click="editarEstagiario(props.dadosEstagiario)"
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
