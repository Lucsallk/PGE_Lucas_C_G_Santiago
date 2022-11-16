<script setup>
import { ref, onMounted } from "vue";
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
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">...</div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
          >
            Close
          </button>
          <button type="button" class="btn btn-primary">Save changes</button>
        </div>
      </div>
    </div>
  </div>
</template>
