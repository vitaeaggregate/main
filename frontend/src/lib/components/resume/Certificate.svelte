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
  export let readOnly: boolean = false;

  onMount(() => {
    if (value.id) return;
    value.id = getRandomId();
  });
</script>

{#if readOnly}
  <div>
    <p><strong>Name:</strong> {value.name ? value.name : ""}</p>
    <p><strong>Description:</strong> {value.description ? value.description : ""}</p>
  </div>
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
