<script>
	import Resume from "$lib/components/resume/Resume.svelte";
	import { checkAccountAndRedirect } from "$lib/store";
	import { page } from "$app/stores";

	// $: resumeId = Number($page.params.id);

	const loadPage = () => {};

	checkAccountAndRedirect(loadPage);
</script>

<section>
	<!-- <h1>Update Resume (id: {resumeId})</h1> -->
	<!-- <Resume bind:id={resumeId}></Resume> -->
</section>
