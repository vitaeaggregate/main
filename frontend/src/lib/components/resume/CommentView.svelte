<script lang="ts">
  import type { Comment } from "$lib/interfaces/resume/Comment";
  import Button from "$lib/components/Button.svelte";
  import { deleteComment } from "$lib/api/comment";
  import CommentComponent from "$lib/components/resume/Comment.svelte";
  import type { Config } from "$lib/components/resume/Comment.svelte";
    import DeleteIconSmall from "$lib/icons/DeleteIconSmall.svelte";

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
    <div class="flex flex-col">
      {#each value as comment (comment.id)}
      <Button><a href="/community/{comment.member}" class="italic">See all comments</a></Button>
        <div class="my-3 flex flex-col gap-3 border-l-8 p-4">
          <CommentComponent bind:value={comment} {config}></CommentComponent>
          {#if comment.can_delete}
          <div class="flex justify-end -mb-5 -mt-3">
        
            <Button on:click={() => comment.id && handleDelete(comment.id)} style="delete"><DeleteIconSmall /></Button></div>
          {/if}
        </div>
      {/each}
    </div>
  {:else}
    <div>
      <p class="p-5 border-l-8 gap-3 my-3"><strong>No Comments</strong></p>
    </div>
  {/if}
{:else if !Array.isArray(value)}
  <CommentComponent bind:value {config}></CommentComponent>
{/if}
