<script lang="ts">
  import InputText from "$lib/components/InputText.svelte";
  import TextArea from "$lib/components/TextArea.svelte";
  import type Skill from "$lib/interfaces/resume/Skill";
  import { getRandomId } from "$lib/utils";
  import { onMount } from "svelte";

  export let value: Skill = {
    name: "",
    description: "",
    skill_level: ""
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
        <strong>{value.name ? value.name : ""}</strong> - {value.skill_level
          ? value.skill_level
          : ""}
      </p>
      <p>
        {value.description
          ? value.description.length
            ? value.description.slice(0, 30)
            : value.description
          : ""}
      </p>
    </div>
  {:else}
    <div>
      <p><strong>Name:</strong> {value.name ? value.name : ""}</p>
      <p><strong>Description:</strong> {value.description ? value.description : ""}</p>
      <p><strong>Skill Level:</strong> {value.skill_level ? value.skill_level : ""}</p>
    </div>
  {/if}
{:else}
  <div>
    <InputText label="Name" required={true} bind:value={value.name} placeholder="Javascript" />
    <TextArea
      label="Description"
      bind:value={value.description}
      placeholder="Frameworks: Svelte, React"
    />
    <InputText label="Skill Level" bind:value={value.skill_level} placeholder="Expert" />
  </div>
{/if}
