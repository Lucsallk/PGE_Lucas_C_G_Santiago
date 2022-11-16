<template>
  <nav class="navbar navbar-expand-lg bg-white">
    <div class="container-fluid justify-content-center justify-content-sm-start">
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
  </nav>
</template>
