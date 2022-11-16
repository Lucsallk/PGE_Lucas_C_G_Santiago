<script setup>
import { getAPI } from "../../assets/axios";
const props = defineProps(["dadosSetor"]);

const editarSetor = (dadosSetor) => {
  getAPI
    .patch("/setores/" + dadosSetor.id + "/", {
      id: dadosSetor.id,
      nome: dadosSetor.nome,
      chefe: dadosSetor.chefe,
      capacidadeSetor: dadosSetor.capacidadeSetor,
    })
    .then(() => {
      location.reload();
    })
    .catch((err) => console.log(err));
};
</script>

<template>
  <div
    class="modal fade"
    id="exampleModal"
    tabindex="-1"
    aria-labelledby="modalSetorEditLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="modalSetorEditLabel">
            Editar Setor
          </h1>
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
                v-model="props.dadosSetor.nome"
                type="text"
                class="form-control"
                id="nome"
              />
            </div>
            <div class="col-4">
              <label for="capacidadeSetor" class="form-label">Capacidade</label>
              <input
                v-model="props.dadosSetor.capacidadeSetor"
                type="number"
                class="form-control"
                id="capacidadeSetor"
              />
            </div>
          </div>
          <div class="row">
            <div class="col-12">
              <label for="capacidadeSetor" class="form-label"
                >Chefe do setor</label
              >
              <input
                v-model="props.dadosSetor.capacidadeSetor"
                type="text"
                class="form-control"
                id="capacidadeSetor"
              />
            </div>
          </div>
        </div>

        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
          >
            Close
          </button>
          <button
            @click="editarSetor(props.dadosSetor)"
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
