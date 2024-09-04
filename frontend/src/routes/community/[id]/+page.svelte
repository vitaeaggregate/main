<script lang="ts">
	import type {BaseComment, Comment} from "$lib/interfaces/resume/Comment";
  	import { onMount } from "svelte";
	import { writable } from "svelte/store";
	import TextArea from "$lib/components/TextArea.svelte"
	import { createComment, getCommentsByMemberIdByResumeId } from "$lib/api/comment";
	import { getResumesByMemberId } from "$lib/api/resume";
	import { account, loadedResumes } from "$lib/store";
	import type {Resume} from "$lib/interfaces/resume/Resume";
	import { goto } from "$app/navigation";
	import { page } from "$app/stores";
	import Resume from "$lib/components/resume/resume.svelte";
	import Comment from "$lib/components/resume/comment.svelte";
	
	export const id = writable<number | null>(null);

		$: resumeId = Number($page.params.id);

	let resumes: Resume[] | null = null;
	let resumesComments: { [resumeId: number]: Comment[] } = {};


	  onMount(async () => {
		if (!$account) return goto("/login/test");
		resumes = await getResumesByMemberId($account.id);
		if (!resumes) return;

		for (let resume of resumes) {
			const comments = await getCommentsByMemberIdByResumeId($account.id, resume.id);
			resumesComments[resume.id] = comments;
			console.log(resumesComments[resume.id])
		}

	});

	function handleCreate(memberId: number, comment: BaseComment) {
 createComment(memberId, comment);
	}
	
</script>
	<main>
	<h1>Community</h1>
	<br/>
	<div class="flex justify-center test-div">

		<div class="w-4/5 h-3/5 bg-gray-200 overflow-y-auto p-6">
			{#if resumes}
			  <p>{#each resumes as resume}
				{#if resume.id === resumeId}
				{Object.entries(resume)}{/if}{/each}
			  </p>
			{/if}
		  </div>
		</div>
		<br /><br />
		<h2>Comments</h2>
		<div class="flex justify-center">
		<div class="w-4/5 h-3/5 overflow-y-auto p-6"><ul class="flex flex-col gap-5 p-5">
			{#each Object.entries(resumesComments) as [id, comments]}
			{#if +id === resumeId}
  <h2>Resume ID: {id}</h2>
  <ul>
    {#each comments as comment}
      <li>{comment.description}</li>
    {/each}
  </ul>{/if}
{/each}
	</div>
		</div>
	<h3>New comment</h3>
<Comment bind:id={resumeId}></Comment>
	</main>