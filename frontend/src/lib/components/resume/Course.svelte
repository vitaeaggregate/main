<script lang="ts">
  import InputText from "$lib/components/InputText.svelte";
  import InputDate from "$lib/components/InputDate.svelte";
  import TextArea from "$lib/components/TextArea.svelte";
  import type Course from "$lib/interfaces/resume/Course";
  import { getRandomId } from "$lib/utils";
  import { onMount } from "svelte";

  export let value: Course = {
    degree: "",
    institution: "",
    city: "",
    country: "",
    start_date: undefined,
    end_date: undefined,
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
        <strong>{value.degree ? value.degree : ""}</strong>, {value.institution
          ? value.institution
          : ""}, {value.country ? value.country : ""}
      </p>
      <p>
        {value.start_date ? value.start_date : ""} - {value.end_date ? value.end_date : ""}
      </p>
    </div>
  {:else}
    <div>
      <p><strong>Degree:</strong> {value.degree ? value.degree : ""}</p>
      <p><strong>Institution:</strong> {value.institution ? value.institution : ""}</p>
      <p><strong>City:</strong> {value.city ? value.city : ""}</p>
      <p><strong>Country:</strong> {value.country ? value.country : ""}</p>
      <p><strong>Start Date:</strong> {value.start_date ? value.start_date : ""}</p>
      <p><strong>End Date:</strong> {value.end_date ? value.end_date : ""}</p>
      <p><strong>Description:</strong> {value.description ? value.description : ""}</p>
    </div>
  {/if}
{:else}
  <div>
    <InputText label="Degree" bind:value={value.degree} placeholder="Business Japanese" />
    <InputText
      label="Institution"
      bind:value={value.institution}
      placeholder="Akamonkai Japanese Language School"
    />
    <InputText label="City" bind:value={value.city} placeholder="Tokyo" />
    <InputText label="Country" bind:value={value.country} placeholder="Japan" />
    <InputDate label="Start Date" bind:value={value.start_date} />
    <InputDate label="End Date" bind:value={value.end_date} />
    <TextArea label="Description" bind:value={value.description} placeholder="Achievements" />
  </div>
{/if}
