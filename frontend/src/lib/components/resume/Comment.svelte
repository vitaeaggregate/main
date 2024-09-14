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
    <div>
      <a href={`/community/${value.header_info && value.header_info.id}`}>
        <strong>Resume Title:</strong>
        {value.header_info && value.header_info.title}
      </a>
    </div>
  {/if}
  <div>
    <p>{value.description}</p>
    <p>{value.created_at && new TimeAgo("en-US").format(new Date(value.created_at))}</p>
  </div>
{:else}
  <div>
    <TextArea bind:value={value.description} label={null}></TextArea>
  </div>
{/if}
