<script lang="ts">
	import { page } from "$app/stores";
	import { createComment } from "$lib/api/comment";
	import type { BaseComment, Comment } from "$lib/interfaces/resume/Comment";
	import { account } from "$lib/store";
	import InputText from "../InputText.svelte";
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

<div>
	<InputText label="Description" bind:value={description} />
	<button on:click={handleCreate}>Submit</button>
</div>
