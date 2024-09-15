<script lang="ts">
  import InputText from "$lib/components/InputText.svelte";
  import TextArea from "$lib/components/TextArea.svelte";
  import type Certificate from "$lib/interfaces/resume/Certificate";
  import { getRandomId } from "$lib/utils";
  import { onMount } from "svelte";

  export let value: Certificate = {
    name: "",
    description: ""
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
        <strong>{value.name ? value.name : ""}</strong>
      </p>
    </div>
  {:else}
    <div>
      <p><strong>Name:</strong> {value.name ? value.name : ""}</p>
      <p><strong>Description:</strong> {value.description ? value.description : ""}</p>
    </div>
  {/if}
{:else}
  <div>
    <InputText
      label="Name"
      bind:value={value.name}
      placeholder="Google Project Management Certification"
    />
    <TextArea
      label="Description"
      bind:value={value.description}
      placeholder="3 month program learning Google's Project Management Techniques"
    />
  </div>
{/if}
