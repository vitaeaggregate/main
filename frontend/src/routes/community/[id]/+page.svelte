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
	
	export const id = writable<number | null>(null);

		$: resumeId = Number($page.params.id);

	let resumes: Resume[] | null = null;
	let resumesComments: { [resumeId: number]: Comment[] } = {};


	  onMount(async () => {
		if (!$account) return goto("/login/test");
		resumes = await getResumesByMemberId($account.id);
		if (!resumes) return;

		for (let resume of resumes) {
			console.log(resumes)
			const comments = await getCommentsByMemberIdByResumeId($account.id, resume.id);
			resumesComments[resume.id] = comments;
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
			{#if resumes}
			{#each resumes as resume}
			<ul class="flex flex-col gap-5 p-5">
					{#each resumesComments[resume.id] as comment}
						<li class="rounded-lg border-2 p-2">
							<p><strong>Member id:</strong> {comment.member}</p>
							<p><strong>Comment:</strong> {comment.description}</p>
						</li>
					{/each}
			</ul>
			{/each}
			{/if}
	</div>
		</div>
	<h3>New comment</h3>
		<div class=" bg-gray-100">
			<form class="p-5">
				<TextArea label="Comment" value=""></TextArea>
			</form>
			<button class="w-28 h-10 bg-slate-200 mt-5 float-right" on:click={() => handleCreate($account.id, _)}>Submit</button>
		</div>
	</main>