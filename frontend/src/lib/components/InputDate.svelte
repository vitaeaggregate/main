<script lang="ts">
  export let label: string = "Input Date";
  export let value: Date | undefined | string;
  export let required: boolean = false;
</script>

<label class="flex flex-col">
  {required ? "*" : ""}
  {label}:
  <input type="date" bind:value class="border-2" />
</label>
