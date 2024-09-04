<script>
	import Resume from "$lib/components/resume/Resume.svelte";
	import { account, checkAccountAndRedirect } from "$lib/store";
	import { page } from "$app/stores";
	import { goto } from "$app/navigation";
	import { browser } from "$app/environment";

	$: resumeId = Number($page.params.id);

	$: {
		if ($account) {
			loadPage();
		} else if (browser) {
			setTimeout(() => goto("/login/test", { replaceState: true }));
		}
	}

	const loadPage = () => {};

	checkAccountAndRedirect(loadPage);
</script>

<section>
	<h1>Update Resume (id: {resumeId})</h1>
	<Resume bind:id={resumeId}></Resume>
</section>
