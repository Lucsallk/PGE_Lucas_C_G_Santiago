<template>
  <nav class="navbar navbar-expand-lg bg-white">
    <div class="container-fluid justify-content-between">
      <router-link
        :to="{ name: 'home' }"
        class="navbar-brand"
        active-class="navbar-brand text-success fw-semibold"
        >Home</router-link
      >
      <p class="navbar-brand fw-semibold m-0">Gestão de Estagiários</p>
    </div>
  </nav>
</template>
