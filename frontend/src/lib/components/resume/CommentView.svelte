<script lang="ts">
  import type { Comment } from "$lib/interfaces/resume/Comment";
  import Button from "$lib/components/Button.svelte";
  import { deleteComment } from "$lib/api/comment";
  import CommentComponent from "$lib/components/resume/Comment.svelte";
  import type { Config } from "$lib/components/resume/Comment.svelte";

  export let value: Comment | Comment[];

  export let config: Config = {
    isReadyOnly: false,
    isResumeTitleHidden: false
  };

  const handleDelete = async (commentId: number | string) => {
    if (!Array.isArray(value)) return;
    const isDeleted = await deleteComment(commentId);
    if (isDeleted) value = value.filter((comment) => commentId !== comment.id);
  };
</script>

{#if Array.isArray(value)}
  {#if value.length}
    <div class="flex flex-col divide-y divide-black">
      {#each value as comment (comment.id)}
        <div class="flex flex-col gap-3 p-4">
          <CommentComponent bind:value={comment} {config}></CommentComponent>
          {#if comment.can_delete}
            <Button on:click={() => comment.id && handleDelete(comment.id)}>Delete</Button>
          {/if}
        </div>
      {/each}
    </div>
  {:else}
    <div>
      <p class="p-5"><strong>No Comments</strong></p>
    </div>
  {/if}
{:else if !Array.isArray(value)}
  <CommentComponent bind:value {config}></CommentComponent>
{/if}
