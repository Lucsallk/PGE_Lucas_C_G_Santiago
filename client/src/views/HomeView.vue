<script setup></script>

<template>
  <main class="mb-auto">
    <div class="container-fluid">
      <div class="row mt-2 mt-sm-5">
        <div class="col-12 col-sm-6 justify-content-center text-center">
          <img class="img-fluid" src="../components/img/pge_logo.jpg" alt="" />
        </div>
        <div class="col-12 col-sm-6 text-center align-self-center">
          <p class="fw-semibold">
            Software desenvolvido para a entrevista de estágio para codin
            utilizando como tecnologia para desenvolvimento Django e Vue.
          </p>
          <p class="fw-semibold">
            Aqui você será capaz de visualizar, adicionar e editar
            <span class="text-success">Estagiários</span> como também alocar
            <span class="text-success">Setores</span>.
          </p>
          <div class="d-flex justify-content-evenly">
            <router-link
              :to="{ name: 'estagiarios' }"
              class="btn btn-success shadow fw-semibold"
              >ESTAGIÁRIOS</router-link
            >
            <router-link
              :to="{ name: 'setores' }"
              class="btn btn-primary shadow fw-semibold"
              >SETORES</router-link
            >
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
