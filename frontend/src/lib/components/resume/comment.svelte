<script lang="ts">
	import { page } from "$app/stores";
	import { createComment, getCommentsByMemberIdByResumeId } from "$lib/api/comment";
	import type { BaseComment, Comment } from "$lib/interfaces/resume/Comment";
	import { account } from "$lib/store";
	import { writable } from "svelte/store";
	import InputText from "../InputText.svelte";
	import TextArea from "../TextArea.svelte";
	let description: string = "";

	export const id: number | null = null;
	$: resumeId = Number($page.params.id);

	async function handleCreate() {
		if (!$account) return;

		const commentObject: BaseComment = {
			header: resumeId,
			member: $account.id,
			description: description
		};

		await createComment($account.id, resumeId, commentObject);
	}



</script>

<div class="bg-gray-200 p-4 mb-4 w-6/12 mx-auto">
	<TextArea label="Description" bind:value={description} />
	<br />
	<button class="border-solid border-2 border-white p-2" on:click={handleCreate}>Submit</button>
</div>
