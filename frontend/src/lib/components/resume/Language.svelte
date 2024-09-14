<script lang="ts">
  import InputText from "$lib/components/InputText.svelte";
  import TextArea from "$lib/components/TextArea.svelte";
  import type Language from "$lib/interfaces/resume/Language";
  import { getRandomId } from "$lib/utils";
  import { onMount } from "svelte";

  export let value: Language = {
    language: "",
    description: "",
    skill_level: ""
  };
  export let readOnly: boolean = false;

  onMount(() => {
    if (value.id) return;
    value.id = getRandomId();
  });
</script>

{#if readOnly}
  <div>
    <p><strong>Language:</strong> {value.language ? value.language : ""}</p>
    <p><strong>Description:</strong> {value.description ? value.description : ""}</p>
    <p><strong>Skill Level:</strong> {value.skill_level ? value.skill_level : ""}</p>
  </div>
{:else}
  <div>
    <InputText label="Language" required={true} bind:value={value.language} placeholder="English"/>
    <TextArea label="Description" required={true} bind:value={value.description} placeholder="Description"/>
    <InputText label="Skill Level" required={true} bind:value={value.skill_level} placeholder="Native"/>
  </div>
{/if}
