<script lang="ts">
	import RichTextComposer from "$lib/components/svelte-lexical/RichTextComposer.svelte";
	import type Comment from "$lib/interfaces/resume/Comment";
  	import { onMount } from "svelte";
	import { writable } from "svelte/store";
	import TextArea from "$lib/components/TextArea.svelte"
	import { getCommentsByMemberIdByResumeId } from "$lib/api/comment";
	import { getResumesByMemberId } from "$lib/api/resume";
	import { account } from "$lib/store";
	import type Resume from "$lib/interfaces/resume/Resume";
	import { goto } from "$app/navigation";
	import { currentResume } from '$lib/store';
	
	export const id = writable<number | null>(null);
	export const resumeId = writable<number | null>(null)

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
			console.log(resumes)
		}
	

	});
	</script>
	<main>
	<h1>Community</h1>
	<br/>
	<div class="flex justify-center test-div">

		<div class="w-4/5 h-3/5 bg-gray-200 overflow-y-auto p-6">
			{#if $currentResume.id}
			  <p><strong>Resume ID:</strong> {$currentResume.id}</p>
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
				<TextArea label="Comment"></TextArea>
			</form>
			<button class="w-28 h-10 bg-slate-200 mt-5 float-right">Submit</button>
		</div>
	</main>

<!-- <section>
	<div class="container">
		<div class="flex justify-center">
			<div class="max-w-4xl rounded-lg border-2">
				<RichTextComposer></RichTextComposer>
			</div>
		</div>
	</div>
	<br/>
	<h2>Comments</h2>
	<div>
	{#each comments as comment}
	<p>{comment.description}</p>
	{/each}
	<p>There is text here</p>
</div>
	
</section> -->