<script lang="ts">
	import { goto } from "$app/navigation";
	import { createResume } from "$lib/api/resume";
	import Resume from "$lib/components/resume/Resume.svelte";
	import type { BaseResume } from "$lib/interfaces/resume/Resume";
	import { account, checkAccountAndRedirect } from "$lib/store";

	let resume: BaseResume = {
		title: "",
		personal_info: {},
		is_shareable: false,
		awards: [],
		certificates: [],
		courses: [],
		educations: [],
		interests: [],
		languages: [],
		links: [],
		professional_exps: [],
		projects: [],
		publications: [],
		references: [],
		skills: []
	};

	const loadPage = () => {};

	const handleCreate = async () => {
		if (!$account || !resume) return;
		resume.member = $account.id;
		resume = await createResume($account.id, resume);
		if (resume) goto("/my/page");
	};

	checkAccountAndRedirect(loadPage);
</script>

<section>
	<h1>New Resume</h1>
	{#if $account}
		<form class="flex flex-col gap-10">
			<Resume bind:value={resume}></Resume>
			<button on:click={handleCreate} class="w-fit"> Add Resume</button>
		</form>
	{/if}
</section>
