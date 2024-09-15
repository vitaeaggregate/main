<script lang="ts">
  import InputText from "$lib/components/InputText.svelte";
  import TextArea from "$lib/components/TextArea.svelte";
  import type Interest from "$lib/interfaces/resume/Interest";
  import { getRandomId } from "$lib/utils";
  import { onMount } from "svelte";

  export let value: Interest = {
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
      required={true}
      bind:value={value.name}
      placeholder="Machine Learning"
    />
    <TextArea
      label="Description"
      bind:value={value.description}
      placeholder="Actively contributing to machine learning dataset"
    />
  </div>
{/if}
