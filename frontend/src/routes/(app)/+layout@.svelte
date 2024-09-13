<script lang="ts">
  import { page } from "$app/stores";
  import Header from "$lib/components/Header.svelte";
  import Footer from "$lib/components/Footer.svelte";
  import { account, checkAccountAndRedirect } from "$lib/store";
  import { onMount } from "svelte";

  onMount(() => checkAccountAndRedirect());

  $: currentPage = $page.url.pathname;

  $: if (currentPage) checkAccountAndRedirect();
</script>

{#if $account}
  <Header></Header>
  <main class="relative -z-10 flex justify-center">
    <div class="container px-10">
      <slot></slot>
    </div>
  </main>
  <Footer></Footer>
{/if}
