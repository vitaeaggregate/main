<script context="module" lang="ts">
  export type CommentNotificationViewType = "full" | "dropdown";
</script>

<script lang="ts">
  import type CommentNotification from "$lib/interfaces/member/CommentNotification";
  import TimeAgo from "javascript-time-ago";
  import Button from "$lib/components/Button.svelte";
  import { dismissNotification } from "$lib/api/commentNotification";
  import { account } from "$lib/store";
  import { goto } from "$app/navigation";
  import CloseIcon from "$lib/icons/CloseIcon.svelte";

  export let value: CommentNotification[] = [];
  export let type: CommentNotificationViewType = "full";

  const handleDismissClick = (notificationId: number) => {
    if (!$account) return;
    value = value.filter((notification) => notification.id !== notificationId);
    dismissNotification($account.id, notificationId);
  };
</script>

{#if value.length}
  <div class="flex flex-col gap-1">
    {#each value as commentNotification (commentNotification.id)}
      {#if type === "full"}
        <div class="mb-2 rounded-xl border-2 bg-white p-2">
          <div class="flex flex-col">
            <p class="flex justify-between">
              <span><strong>Resume Id: </strong>{commentNotification.header.id}</span>
              <span class="mx-4">
                <Button on:click={() => handleDismissClick(commentNotification.id)} style="default"
                  ><CloseIcon /></Button
                >
              </span>
            </p>
            <p>
              <a href={"/community/" + commentNotification.header.id}>
                <strong>Resume Title: </strong>
                <span class="text-blue-700 underline underline-offset-4">
                  {commentNotification.header.title}
                </span>
              </a>
            </p>
            <p><strong>Comment: </strong>{commentNotification.comment.description}</p>
            <p>
              <strong>Created: </strong>{new TimeAgo("en-US").format(
                new Date(commentNotification.created_at)
              )}
            </p>
          </div>
        </div>
      {:else if type === "dropdown"}
        <div
          class="rounded-lg border-2 p-4"
          role="button"
          aria-hidden="true"
          tabindex="0"
          on:click={() => goto("/community/" + commentNotification.header.id)}
        >
          <p>
            <strong>Title: </strong>{commentNotification.header.title}
          </p>
          <p>
            <strong>Comment: </strong>
            {#if commentNotification.comment.description}
              {commentNotification.comment.description.length > 10
                ? commentNotification.comment.description.substring(0, 10) + "..."
                : commentNotification.comment.description}
            {/if}
          </p>
          <p class="text-sm">
            {new TimeAgo("en-US").format(new Date(commentNotification.created_at))}
          </p>
        </div>
      {/if}
    {/each}
  </div>
{:else}
  <div>
    <p>Nothing new for now.</p>
  </div>
{/if}
