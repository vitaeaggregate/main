<script context="module" lang="ts">
  export interface Config {
    isReadyOnly?: boolean;
    isResumeTitleHidden?: boolean;
  }
</script>

<script lang="ts">
  import type { Comment } from "$lib/interfaces/resume/Comment";
  import { getRandomId } from "$lib/utils";
  import { onMount } from "svelte";
  import TextArea from "$lib/components/TextArea.svelte";
  import TimeAgo from "javascript-time-ago";

  export let value: Comment = {
    description: "",
    created_at: ""
  };

  export let config: Config = {
    isReadyOnly: false,
    isResumeTitleHidden: false
  };

  onMount(() => {
    if (value.id) return;
    value.id = getRandomId();
  });
</script>

{#if config.isReadyOnly}
  {#if !config.isResumeTitleHidden}
    <p class="underline underline-offset-4">
      <a href={`/community/${value.header_info && value.header_info.id}`}>
        <strong>Resume Title:</strong>
        {value.header_info && value.header_info.title}
      </a>
    </p>
  {/if}
  <div class="flex flex-col gap-3">
    <p>{value.description}</p>
    <p class="self-end italic">
      {value.created_at && new TimeAgo("en-US").format(new Date(value.created_at))}
    </p>
  </div>
{:else}
  <div>
    <TextArea bind:value={value.description} label={null}></TextArea>
  </div>
{/if}
