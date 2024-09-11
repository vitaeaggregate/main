<script>
	import { goto } from "$app/navigation";
	import { account, checkAccountAndRedirect } from "$lib/store";
	import Logo from "$lib/Logo.png";
	import { onMount } from "svelte";

	checkAccountAndRedirect(() => goto("/my/page"));

  </script>
  
  <section class="flex md:flex-row flex-col justify-center lg:items-center md:items-center px-10">
  </section>