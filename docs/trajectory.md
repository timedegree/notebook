---
title: 轨迹
changelog: True
---

<div class="trajectory">

<input class="traj-radio" type="radio" name="traj-tab" id="traj-tab-1" checked>
<input class="traj-radio" type="radio" name="traj-tab" id="traj-tab-2">
<input class="traj-radio" type="radio" name="traj-tab" id="traj-tab-3">

<div class="traj-switch">
    <span class="traj-thumb" aria-hidden="true"></span>
    <label class="traj-seg" for="traj-tab-1">足迹 / timeline</label>
    <label class="traj-seg" for="traj-tab-2">战绩 / awards</label>
    <label class="traj-seg" for="traj-tab-3">更新记录 / changelog</label>
</div>

<div class="traj-panels">

<section class="traj-panel traj-panel-timeline">
{{ TIMELINE }}
</section>

<section class="traj-panel traj-panel-awards">
{{ AWARDS }}
</section>

<section class="traj-panel traj-panel-changelog">
<h2 class="traj-year">2025</h2>
{{ 2025 }}

<h2 class="traj-year">2024</h2>
{{ 2024 }}

<h2 class="traj-year">2023</h2>
{{ 2023 }}

<h2 class="traj-year">2022</h2>
{{ 2022 }}
</section>

</div>
</div>
