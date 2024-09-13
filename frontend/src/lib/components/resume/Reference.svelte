<script lang="ts">
  import { createEventDispatcher } from "svelte";
  import InputText from "$lib/components/InputText.svelte";
  import type Reference from "$lib/interfaces/resume/Reference";
  import { getRandomId } from "$lib/utils";
  import { onMount } from "svelte";

  export let value: Reference = {
    name: "",
    job_title: "",
    organization: "",
    email: "",
    phone: ""
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
    <p><strong>Job Title:</strong> {value.job_title ? value.job_title : ""}</p>
    <p><strong>Organization:</strong> {value.organization ? value.organization : ""}</p>
    <p><strong>Email:</strong> {value.email ? value.email : ""}</p>
    <p><strong>Phone:</strong> {value.phone ? value.phone : ""}</p>
  </div>
{:else}
  <div>
    <InputText label="Name" required={true} bind:value={value.name} placeholder="Clark Kent"/>
    <InputText label="Job Title" bind:value={value.job_title} placeholder="Reporter"/>
    <InputText label="Organization" bind:value={value.organization} placeholder="Daily Planet"/>
    <InputText label="Email" bind:value={value.email} placeholder="clark.kent@dailyplanet.com"/>
    <InputText label="Phone" bind:value={value.phone} placeholder="XXX-XXXX-XXXX"/>
  </div>
{/if}
