---
title: Home
hide:
    - date
    - toc
    - title
    - navigation
home: true
statistics: true
---

<link rel="stylesheet" href="css/index.css">

<div class="hero-section">
    <div class="hero-text">
        <h1 class="hero-title">Hi! _(:ɜ⌋∠)_</h1>
        <p class="hero-desc">
            这里是 <strong>时度度 (TimeDegree)</strong> 的笔记本。<br>
            用于存放 CS、Math 和 CTF 相关的专业笔记，与 <a href="https://blog.timedegree.cc">博客</a> 区分开来。
        </p>
        <div class="hero-actions">
            <a href="https://blog.timedegree.cc/about" class="md-button md-button--primary">关于我</a>
            <a href="https://github.com/timedegree" class="md-button">GitHub</a>
        </div>
    </div>
    <div class="hero-image">
        <img src="assets/logo-Hymmn0s.png" alt="TimeDegree Logo">
    </div>
</div>

<div class="dashboard-grid">
    <a href="changelog" class="feature-card">
        <div class="card-icon">
            <span class="twemoji">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 20a8 8 0 0 0 8-8 8 8 0 0 0-8-8 8 8 0 0 0-8 8 8 8 0 0 0 8 8m0-18a10 10 0 0 1 10 10 10 10 0 0 1-10 10C6.47 22 2 17.5 2 12S6.5 2 12 2m.5 5v5.25l4.5 2.67-.75 1.23L11 13V7h1.5Z"/></svg>
            </span>
        </div>
        <div class="card-title">最近更新</div>
        <div class="card-desc">
            查看笔记本的变更日志与修订历史。
        </div>
    </a>

    <a href="links" class="feature-card">
        <div class="card-icon">
            <span class="twemoji">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M10.59 13.41c.41.39.41 1.03 0 1.42-.39.39-1.03.39-1.42 0a5.003 5.003 0 0 1 0-7.07l3.54-3.54a5.003 5.003 0 0 1 7.07 0 5.003 5.003 0 0 1 0 7.07l-1.49 1.49c.01-.82-.12-1.64-.4-2.42l.47-.48a2.982 2.982 0 0 0 0-4.24 2.982 2.982 0 0 0-4.24 0l-3.53 3.53a2.982 2.982 0 0 0 0 4.24m2.82-4.24c.39-.39 1.03-.39 1.42 0a5.003 5.003 0 0 1 0 7.07l-3.54 3.54a5.003 5.003 0 0 1-7.07 0 5.003 5.003 0 0 1 0-7.07l1.49-1.49c-.01.82.12 1.64.4 2.42l-.47.48a2.982 2.982 0 0 0 0 4.24 2.982 2.982 0 0 0 4.24 0l3.53-3.53a2.982 2.982 0 0 0 0-4.24.973.973 0 0 1 0-1.42Z"/></svg>
            </span>
        </div>
        <div class="card-title">朋友们！</div>
        <div class="card-desc">
            友情链接、致谢以及那些有趣的人。
        </div>
    </a>

    <a href="javascript:toggle_statistics();" class="feature-card">
        <div class="card-icon">
            <span class="twemoji">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M22 21H2V3h2v16h18v2M10 17l-5-5 5-5v10m4 0V7l5 5-5 5Z"/></svg>
            </span>
        </div>
        <div class="card-title">站点统计</div>
        <div class="card-desc">
            点击查看本站的文章数、代码行数及运行时间。
        </div>
    </a>
</div>

<div id="statistics">
    <div class="statistics-wrapper">
        <div class="stat-item">页面总数：{{pages}}</div>
        <div class="stat-item">总字数：{{words}}</div>
        <div class="stat-item">代码块行数：{{codes}}</div>
        <div class="stat-item">网站运行时间：<span id="web-time"></span></div>
    </div>
</div>

<script>
function updateTime() {
    var date = new Date();
    var now = date.getTime();
    var startDate = new Date("2022/08/22 13:07:15");
    var start = startDate.getTime();
    var diff = now - start;
    var y, d, h, m;
    y = Math.floor(diff / (365 * 24 * 3600 * 1000));
    diff -= y * 365 * 24 * 3600 * 1000;
    d = Math.floor(diff / (24 * 3600 * 1000));
    h = Math.floor(diff / (3600 * 1000) % 24);
    m = Math.floor(diff / (60 * 1000) % 60);
    if (y == 0) {
        document.getElementById("web-time").innerHTML = d + "<span class=\"heti-spacing\"> </span>天<span class=\"heti-spacing\"> </span>" + h + "<span class=\"heti-spacing\"> </span>小时<span class=\"heti-spacing\"> </span>" + m + "<span class=\"heti-spacing\"> </span>分钟";
    } else {
        document.getElementById("web-time").innerHTML = y + "<span class=\"heti-spacing\"> </span>年<span class=\"heti-spacing\"> </span>" + d + "<span class=\"heti-spacing\"> </span>天<span class=\"heti-spacing\"> </span>" + h + "<span class=\"heti-spacing\"> </span>小时<span class=\"heti-spacing\"> </span>" + m + "<span class=\"heti-spacing\"> </span>分钟";
    }
    setTimeout(updateTime, 1000 * 60);
}
updateTime();

function toggle_statistics() {
    var statistics = document.getElementById("statistics");
    statistics.classList.toggle("show");
}
</script>
