<script>
	import { goto } from "$app/navigation";
	import { checkAccountAndRedirect } from "$lib/store";

	checkAccountAndRedirect(() => goto("/my/page"));
</script>
