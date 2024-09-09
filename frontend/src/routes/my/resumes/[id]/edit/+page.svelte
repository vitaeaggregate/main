<script lang="ts">
	import { page } from "$app/stores";
	import { getResumesByResumeId } from "$lib/api/resume";
	import { checkAccountAndRedirect } from "$lib/store";

	$: resumeId = Number($page.params.id);

	const loadPage = async () => {
		const resume = await getResumesByResumeId(resumeId);

		console.log(resume);
	};

	checkAccountAndRedirect(loadPage);
</script>
