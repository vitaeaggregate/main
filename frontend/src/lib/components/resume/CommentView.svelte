<script context="module" lang="ts">
	export interface Config {
		isReadyOnly: boolean;
	}
</script>

<script lang="ts">
	import type { Comment } from "$lib/interfaces/resume/Comment";
	import Button from "$lib/components/Button.svelte";
	import { deleteComment } from "$lib/api/comment";

	export let value: Comment[];

	export let config: Config = {
		isReadyOnly: true
	};

	const handleDelete = (commentId: number) => {
		deleteComment(commentId);
		value = value.filter((comment) => commentId !== comment.id);
	};
</script>

{#if config.isReadyOnly}
	{#if value.length}
		<div class="flex flex-col divide-y divide-black">
			{#each value as comment (comment.id)}
				<div class="flex flex-col gap-2 p-4">
					<p>
						<a href={comment.header && `/community/${comment.header.id}`}>
							<strong>Resume Title:</strong>
							{comment.header && comment.header.title}
						</a>
					</p>
					<div>
						<p><strong>Comment:</strong></p>
						<p>{comment.description}</p>
					</div>
					<Button on:click={() => handleDelete(comment.id)}>Delete</Button>
				</div>
			{/each}
		</div>
	{:else}
		<p class="p-5"><strong>No Comments</strong></p>
	{/if}
{/if}
