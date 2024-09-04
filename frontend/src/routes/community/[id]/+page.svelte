<script lang="ts">
	import type { Comment } from "$lib/interfaces/resume/Comment";
	import { writable } from "svelte/store";
	import { getCommentsByMemberIdByResumeId } from "$lib/api/comment";
	import { getResumesByMemberId } from "$lib/api/resume";
	import { account, checkAccountAndRedirect, loadedResumes } from "$lib/store";
	import type { Resume } from "$lib/interfaces/resume/Resume";
	import { page } from "$app/stores";
	import NewComment from "$lib/components/resume/comment.svelte";

	export const id = writable<number | null>(null);

	$: resumeId = Number($page.params.id);

	let resumes: Resume[] | null = null;
	let resumesComments: { [resumeId: number]: Comment[] } = {};

	const loadPage = async () => {
		if (!$account) return;
		resumes = await getResumesByMemberId($account.id);

		for (let resume of resumes) {
			const comments = await getCommentsByMemberIdByResumeId($account.id, resume.id);
			resumesComments[resume.id] = comments;
		}
	};

	checkAccountAndRedirect(loadPage);
</script>

<main>
	<h1>Community</h1>
	<br />
	<div class="test-div flex justify-center">
		<div class="h-3/5 w-4/5 overflow-y-auto bg-gray-200 p-6">
			{#if resumes}
				<p>
					{#each resumes as resume}
						{#if resume.id === resumeId}
							{Object.entries(resume)}
						{/if}
					{/each}
				</p>
			{/if}
		</div>
		<br /><br />
		<h2>Comments</h2>
		<div class="flex justify-center">
		<div class="w-4/5 h-3/5 overflow-y-auto p-6"><ul class="flex flex-col gap-5 p-5">
			{#each Object.entries(resumesComments) as [id, comments]}
			{#if +id === resumeId}
  <h2>Resume ID: {id}</h2>
  <ul>
    {#each comments as comment, index}
      <li class="bg-gray-200 p-4">{index + 1}: {comment.description}</li><br/>
    {/each}
  </ul>{/if}
{/each}
	</div>
	<br /><br />
	<h2>Comments</h2>
	<div class="flex justify-center">
		<div class="h-3/5 w-4/5 overflow-y-auto p-6">
			<ul class="flex flex-col gap-5 p-5">
				{#each Object.entries(resumesComments) as [id, comments]}
					{#if +id === resumeId}
						<h2>Resume ID: {id}</h2>
						<ul>
							{#each comments as comment}
								<li>{comment.description}</li>
							{/each}
						</ul>{/if}
				{/each}
			</ul>
		</div>
	</div>
	<h3>New comment</h3>
	<NewComment></NewComment>
</main>
