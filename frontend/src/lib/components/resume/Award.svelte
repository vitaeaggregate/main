<script lang="ts">
  import InputText from "$lib/components/InputText.svelte";
  import InputDate from "$lib/components/InputDate.svelte";
  import TextArea from "$lib/components/TextArea.svelte";
  import type Award from "$lib/interfaces/resume/Award";
  import { getRandomId } from "$lib/utils";
  import { onMount } from "svelte";

  export let value: Award = {
    title: "",
    issuer: "",
    description: "",
    date: ""
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
        <strong>{value.title ? value.title : ""}</strong>, {value.issuer ? value.issuer : ""}, {value.issuer
          ? value.issuer
          : ""}
      </p>
      <p>
        {value.date ? value.date : ""}
      </p>
    </div>
  {:else}
    <div>
      <p><strong>Title:</strong> {value.title ? value.title : ""}</p>
      <p><strong>Issuer:</strong> {value.issuer ? value.issuer : ""}</p>
      <p><strong>Date:</strong> {value.date ? value.date : ""}</p>
      <p><strong>Description:</strong> {value.description ? value.description : ""}</p>
    </div>
  {/if}
{:else}
  <div>
    <InputText label="Title" bind:value={value.title} placeholder="Excellence in Management" />
    <InputText label="Issuer" bind:value={value.issuer} placeholder="ACME Software" />
    <InputDate label="Date" bind:value={value.date} />
    <TextArea
      label="Description"
      bind:value={value.description}
      placeholder="Awarded for outstanding performance as team lead"
    />
  </div>
{/if}
