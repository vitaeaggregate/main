<script>
	import { goto } from "$app/navigation";
	import { account, checkAccountAndRedirect } from "$lib/store";
	import Logo from "$lib/Logo.png";
	import { onMount } from "svelte";

	checkAccountAndRedirect(() => goto("/my/page"));

  </script>