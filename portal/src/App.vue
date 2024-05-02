

<template>
<div>
<div class="navbar-container">
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">
      <img src="/src/assets/logo.svg" alt="Logo" width="30" height="30" class="d-inline-block align-text-top">
    </a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/">CV Ranker</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dummy
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="/document">Test</a></li>
            <li><a class="dropdown-item" href="#">Test2</a></li>
            <li><a class="dropdown-item" href="#">Test3</a></li>
          </ul>
        </li>
      </ul>
      <form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
</div>
  <div class="container">
    <div class="row">
      <div class="col-12">
        <RouterView></RouterView>
      </div>
    </div>
  </div>
</div>
</template>

<script setup>

</script>


<style scoped>
.navbar-nav .nav-link {
  color: #582B8C;
}

.navbar-nav .nav-link:hover {
  border-bottom: 2px solid #582B8C;
}
</style>
