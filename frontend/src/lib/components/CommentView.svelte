<script context="module" lang="ts">
	export interface Config {
		isReadyOnly: boolean;
	}
</script>

<script lang="ts">
	import type { Comment } from "$lib/interfaces/resume/Comment";

	export let value: Comment[];

	export let config: Config = {
		isReadyOnly: true
	};
</script>

{#if config.isReadyOnly}
	{#if value.length}
		<div>
			{#each value as comment (comment.id)}
				<div>
					<p>{comment}</p>
					<p>{comment.description}</p>
				</div>
			{/each}
		</div>
	{/if}
{/if}
