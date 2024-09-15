<script lang="ts">
  import InputText from "$lib/components/InputText.svelte";
  import type Link from "$lib/interfaces/resume/Link";
  import { getRandomId } from "$lib/utils";
  import { onMount } from "svelte";

  export let value: Link = {
    title: "",
    url: ""
  };
  export let readOnly = false;
  export let isList = false;

  onMount(() => {
    if (value.id) return;
    value.id = getRandomId();
  });
</script>

{#if readOnly}
  {#if isList}
    <div>
      <p>
        <strong>{value.title ? value.title : ""}</strong>
      </p>
      <p>
        {value.url ? (value.url.length > 10 ? value.url.slice(0, 30) + "..." : value.url) : ""}
      </p>
    </div>
  {:else}
    <div>
      <p><strong>Title:</strong> {value.title ? value.title : ""}</p>
      <p><strong>URL:</strong> {value.url ? value.url : ""}</p>
    </div>
  {/if}
{:else}
  <div>
    <InputText
      label="Title"
      required={true}
      bind:value={value.title}
      placeholder="LinkedIn/Github/Portfolio"
    />
    <InputText
      label="URL"
      required={true}
      bind:value={value.url}
      placeholder="ex. linkedin.com/stevesmith"
    />
  </div>
{/if}
