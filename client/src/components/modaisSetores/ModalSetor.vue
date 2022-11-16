<script setup>
import { ref } from "vue";
import { getAPI } from "../../assets/axios";
const nome = ref("");
const chefe = ref("");
const capacidadeSetor = ref("");

const adicionarSetores = () => {
  getAPI
    .post("/setores/", {
      nome: nome.value,
      chefe: chefe.value,
      capacidadeSetor: capacidadeSetor.value,
    })
    .then((response) => {
      console.log(response);
      location.reload();
    })
    .catch((err) => console.log(err));
};
</script>
<template>
  <div
    class="modal fade"
    id="setorModal"
    tabindex="-1"
    aria-labelledby="cadModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="cadModalLabel">Adicionar Setor</h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>

        <div class="modal-body">
          <div class="row mb-3">
            <div class="col-8">
              <label for="nome" class="form-label">Nome do setor</label>
              <input
                v-model="nome"
                id="nome"
                class="form-control"
                type="text"
              />
            </div>
            <div class="col-4">
              <label for="capacidadeSetor" class="form-label">Capacidade</label>
              <input
                v-model="capacidadeSetor"
                id="capacidadeSetor"
                class="form-control"
                type="number"
              />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-12">
              <label for="nome" class="form-label">Chefe do setor</label>
              <input
                v-model="chefe"
                id="nome"
                class="form-control"
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
            @click="adicionarSetores"
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
