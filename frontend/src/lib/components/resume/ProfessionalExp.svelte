<script lang="ts">
  import TextArea from "$lib/components/TextArea.svelte";
  import InputText from "$lib/components/InputText.svelte";
  import InputDate from "$lib/components/InputDate.svelte";
  import type ProfessionalExp from "$lib/interfaces/resume/ProfessionalExp";
  import { getRandomId } from "$lib/utils";
  import { onMount } from "svelte";

  export let value: ProfessionalExp = {
    job_title: "",
    employer: "",
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
        <strong>{value.job_title ? value.job_title : ""}</strong>, {value.employer
          ? value.employer
          : ""}, {value.country ? value.country : ""}
      </p>
    </div>
  {:else}
    <div>
      <p><strong>Job Title:</strong> {value.job_title ? value.job_title : ""}</p>
      <p><strong>Employer:</strong> {value.employer ? value.employer : ""}</p>
      <p><strong>City:</strong> {value.city ? value.city : ""}</p>
      <p><strong>Country:</strong> {value.country ? value.country : ""}</p>
      <p><strong>Start Date:</strong> {value.start_date ? value.start_date : ""}</p>
      <p><strong>End Date:</strong> {value.end_date ? value.end_date : ""}</p>
      <p><strong>Description:</strong></p>
      <p class="whitespace-pre-line">{value.description ? value.description : ""}</p>
    </div>
  {/if}
{:else}
  <div>
    <InputText
      label="Job Title"
      required={true}
      bind:value={value.job_title}
      placeholder="QA Tester"
    />
    <InputText
      label="Employer"
      required={true}
      bind:value={value.employer}
      placeholder="ACME Software"
    />
    <InputText label="City" bind:value={value.city} placeholder="Tokyo" />
    <InputText label="Country" bind:value={value.country} placeholder="Japan" />
    <InputDate label="Start Date" bind:value={value.start_date} />
    <InputDate label="End Date" bind:value={value.end_date} />
    <TextArea
      label="Description"
      required={true}
      bind:value={value.description}
      placeholder="Listed Experience"
    />
  </div>
{/if}
