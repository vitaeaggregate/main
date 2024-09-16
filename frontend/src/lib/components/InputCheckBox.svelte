<script lang="ts">
  export let label: string | null = null;
  export let value: boolean = false;
</script>

<label class="flex items-center">
  <input type="checkbox" bind:checked={value} />
  <span class="mx-2">{label ? label : ""}</span>
</label>
