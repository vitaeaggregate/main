<script lang="ts">
	import { goto } from "$app/navigation";
	import { page } from "$app/stores";
	import { getResumeById, updateResume } from "$lib/api/resume";
	import MainButton from "$lib/components/MainButton.svelte";
	import ResumeComponent from "$lib/components/resume/Resume.svelte";
	import type { Resume } from "$lib/interfaces/resume/Resume";
	import { account, checkAccountAndRedirect } from "$lib/store";

	let resume: Resume | null = null;

	const loadResume = async () => {
		if (!$account || !$page.params.id) return;
		resume = await getResumeById(Number($page.params.id));
	};

	const handleSaveClick = async () => {
		if (!$account || !resume) return;
		const updatedResume: Resume = await updateResume(resume);
		resume = updatedResume;
	};

	const handleCancelClick = () => {
		goto(`/my/resumes/${resume?.id}`);
	};

	$: if ($page.params.id && $account) loadResume();

	checkAccountAndRedirect();
</script>

<section>
	<h1>Edit Resume</h1>
	<br />
	{#if resume}
		<ResumeComponent bind:value={resume}></ResumeComponent><br />
		<MainButton on:click={handleCancelClick}>Cancel</MainButton>
		<MainButton on:click={handleSaveClick}>Save</MainButton>
	{/if}
</section>
