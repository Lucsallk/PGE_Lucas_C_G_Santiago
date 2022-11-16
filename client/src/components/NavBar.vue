<template>
  <nav class="navbar navbar-expand-lg bg-white">
    <div class="container-fluid justify-content-between">
      <div>
        <router-link
          :to="{ name: 'home' }"
          class="navbar-brand"
          active-class="navbar-brand text-success fw-semibold"
          >Home</router-link
        >
        <router-link
          :to="{ name: 'estagiarios' }"
          class="navbar-brand"
          active-class="navbar-brand text-success fw-semibold"
          >Estagiário</router-link
        >
        <router-link
          :to="{ name: 'setores' }"
          class="navbar-brand"
          active-class="navbar-brand text-success fw-semibold"
          >Setores</router-link
        >
      </div>
      <p class="navbar-brand fw-semibold m-0">Gestão de Estagiários</p>
    </div>
  </nav>
</template>
