<script lang="ts">
  import InputText from "$lib/components/InputText.svelte";
  import InputDate from "$lib/components/InputDate.svelte";
  import type Project from "$lib/interfaces/resume/Project";
  import { getRandomId } from "$lib/utils";
  import { onMount } from "svelte";
  import TextArea from "$lib/components/TextArea.svelte";

  export let value: Project = {
    title: "",
    sub_title: "",
    start_date: undefined,
    end_date: undefined,
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
    <p><strong>Title:</strong> {value.title ? value.title : ""}</p>
    <p><strong>Subtitle:</strong> {value.sub_title ? value.sub_title : ""}</p>
    <p><strong>Start Date:</strong> {value.start_date ? value.start_date : ""}</p>
    <p><strong>End Date:</strong> {value.end_date ? value.end_date : ""}</p>
    <p><strong>Description:</strong></p>
    <p class="whitespace-pre-line">{value.description ? value.description : ""}</p>
  </div>
{:else}
  <div>
    <InputText
      label="Title"
      required={true}
      bind:value={value.title}
      placeholder="Fullstack Project"
    />
    <InputText label="Subtitle" bind:value={value.sub_title} placeholder="Fullstack Engineer" />
    <InputDate label="Start Date" bind:value={value.start_date} />
    <InputDate label="End Date" bind:value={value.end_date} />
    <TextArea
      label="Description"
      required={true}
      bind:value={value.description}
      placeholder="built fullstack project as a member of 5 person team. Focused on Frontend and used Svelte and used Django in the backend"
    />
  </div>
{/if}
