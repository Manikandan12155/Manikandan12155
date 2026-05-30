
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; }

body { font-family: 'Space Grotesk', sans-serif; }

.portfolio {
  background: #0a0a0f;
  color: #e2e8f0;
  min-height: 100vh;
  font-family: 'Space Grotesk', sans-serif;
  padding: 0;
  border-radius: 16px;
  overflow: hidden;
}

.hero {
  background: linear-gradient(135deg, #0d0d1a 0%, #0f172a 40%, #0d1f3c 100%);
  padding: 60px 48px 50px;
  position: relative;
  border-bottom: 1px solid rgba(112, 165, 253, 0.15);
  overflow: hidden;
}

.hero::before {
  content: '';
  position: absolute;
  top: -80px; right: -80px;
  width: 320px; height: 320px;
  background: radial-gradient(circle, rgba(112,165,253,0.12) 0%, transparent 70%);
  border-radius: 50%;
}

.hero::after {
  content: '';
  position: absolute;
  bottom: -60px; left: 60px;
  width: 200px; height: 200px;
  background: radial-gradient(circle, rgba(191,145,243,0.1) 0%, transparent 70%);
  border-radius: 50%;
}

.hero-top {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 32px;
  position: relative;
  z-index: 1;
}

.hero-badge {
  background: rgba(112,165,253,0.12);
  border: 1px solid rgba(112,165,253,0.25);
  color: #70a5fd;
  font-size: 12px;
  font-weight: 500;
  padding: 6px 14px;
  border-radius: 20px;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  font-family: 'JetBrains Mono', monospace;
}

.status-dot {
  display: inline-block;
  width: 7px; height: 7px;
  background: #38bdae;
  border-radius: 50%;
  margin-right: 6px;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.4; }
}

.hero-name {
  font-size: 56px;
  font-weight: 700;
  color: #fff;
  letter-spacing: -1.5px;
  line-height: 1;
  margin-bottom: 8px;
  position: relative; z-index: 1;
}

.hero-name span {
  background: linear-gradient(90deg, #70a5fd, #bf91f3);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-role {
  font-size: 18px;
  color: #8b949e;
  font-weight: 400;
  margin-bottom: 28px;
  position: relative; z-index: 1;
}

.hero-role strong { color: #c9d1d9; font-weight: 500; }

.hero-links {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  position: relative; z-index: 1;
}

.hero-link {
  display: flex;
  align-items: center;
  gap: 6px;
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.1);
  color: #c9d1d9;
  text-decoration: none;
  font-size: 13px;
  padding: 8px 16px;
  border-radius: 8px;
  font-weight: 400;
  transition: all 0.2s;
  cursor: pointer;
  font-family: 'JetBrains Mono', monospace;
}

.hero-link:hover {
  background: rgba(112,165,253,0.1);
  border-color: rgba(112,165,253,0.3);
  color: #70a5fd;
}

.hero-link i { font-size: 15px; }

.section {
  padding: 36px 48px;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}

.section-label {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: #70a5fd;
  margin-bottom: 24px;
  font-family: 'JetBrains Mono', monospace;
}

.section-label::after {
  content: '';
  flex: 1;
  height: 1px;
  background: rgba(112,165,253,0.2);
}

.code-block {
  background: #0d1117;
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 12px;
  padding: 24px 28px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  line-height: 1.8;
  overflow: hidden;
  position: relative;
}

.code-block::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 2px;
  background: linear-gradient(90deg, #70a5fd, #bf91f3, #38bdae);
}

.code-top {
  display: flex;
  gap: 6px;
  margin-bottom: 18px;
}

.dot { width: 10px; height: 10px; border-radius: 50%; }
.dot-r { background: #ff5f57; }
.dot-y { background: #febc2e; }
.dot-g { background: #28c840; }

.kw { color: #bf91f3; }
.cn { color: #70a5fd; }
.str { color: #a5d6ff; }
.cm { color: #484f58; }
.fn { color: #38bdae; }
.op { color: #8b949e; }
.num { color: #f78166; }

.tech-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 8px;
}

.tech-badge {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 8px;
  padding: 10px 14px;
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  color: #c9d1d9;
  font-weight: 400;
  transition: all 0.2s;
  cursor: default;
}

.tech-badge:hover {
  background: rgba(112,165,253,0.08);
  border-color: rgba(112,165,253,0.2);
  color: #e2e8f0;
}

.tech-dot {
  width: 8px; height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}

.cat-label {
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #484f58;
  font-family: 'JetBrains Mono', monospace;
  margin: 20px 0 10px;
}

.exp-cards {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.exp-card {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 12px;
  padding: 20px 24px;
  position: relative;
  overflow: hidden;
  transition: all 0.2s;
  cursor: default;
}

.exp-card::before {
  content: '';
  position: absolute;
  left: 0; top: 0; bottom: 0;
  width: 3px;
  background: linear-gradient(180deg, #70a5fd, #bf91f3);
}

.exp-card:hover {
  background: rgba(112,165,253,0.04);
  border-color: rgba(112,165,253,0.15);
}

.exp-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 6px;
  flex-wrap: wrap;
  gap: 8px;
}

.exp-company {
  font-weight: 600;
  font-size: 15px;
  color: #e2e8f0;
}

.exp-date {
  font-size: 12px;
  color: #484f58;
  font-family: 'JetBrains Mono', monospace;
  background: rgba(255,255,255,0.04);
  padding: 3px 10px;
  border-radius: 4px;
}

.exp-role {
  font-size: 13px;
  color: #70a5fd;
  font-weight: 500;
  margin-bottom: 12px;
}

.exp-points {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.exp-points li {
  font-size: 13px;
  color: #8b949e;
  padding-left: 16px;
  position: relative;
  line-height: 1.5;
}

.exp-points li::before {
  content: '→';
  position: absolute;
  left: 0;
  color: #38bdae;
  font-size: 11px;
}

.proj-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.proj-card {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 12px;
  padding: 20px;
  transition: all 0.2s;
  cursor: default;
  position: relative;
  overflow: hidden;
}

.proj-card::after {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(112,165,253,0.4), transparent);
  opacity: 0;
  transition: opacity 0.3s;
}

.proj-card:hover {
  background: rgba(112,165,253,0.05);
  border-color: rgba(112,165,253,0.18);
  transform: translateY(-1px);
}

.proj-card:hover::after { opacity: 1; }

.proj-client {
  font-size: 10px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #38bdae;
  font-family: 'JetBrains Mono', monospace;
  margin-bottom: 6px;
}

.proj-name {
  font-size: 15px;
  font-weight: 600;
  color: #e2e8f0;
  margin-bottom: 8px;
}

.proj-desc {
  font-size: 12px;
  color: #6e7681;
  line-height: 1.5;
  margin-bottom: 12px;
}

.proj-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
}

.proj-tag {
  background: rgba(112,165,253,0.08);
  border: 1px solid rgba(112,165,253,0.15);
  color: #70a5fd;
  font-size: 10px;
  padding: 2px 8px;
  border-radius: 4px;
  font-family: 'JetBrains Mono', monospace;
}

.stats-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
}

.stat-card {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 10px;
  padding: 16px;
  text-align: center;
}

.stat-num {
  font-size: 28px;
  font-weight: 700;
  color: #70a5fd;
  font-family: 'JetBrains Mono', monospace;
  display: block;
  margin-bottom: 4px;
}

.stat-label {
  font-size: 11px;
  color: #484f58;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.footer {
  padding: 28px 48px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
  background: rgba(0,0,0,0.2);
}

.footer-text {
  font-size: 12px;
  color: #484f58;
  font-family: 'JetBrains Mono', monospace;
}

.footer-actions {
  display: flex;
  gap: 8px;
}

.btn {
  display: flex;
  align-items: center;
  gap: 6px;
  background: rgba(112,165,253,0.1);
  border: 1px solid rgba(112,165,253,0.25);
  color: #70a5fd;
  font-size: 12px;
  padding: 8px 16px;
  border-radius: 7px;
  cursor: pointer;
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 500;
  transition: all 0.2s;
}

.btn:hover {
  background: rgba(112,165,253,0.2);
  border-color: rgba(112,165,253,0.4);
}

.btn i { font-size: 14px; }
</style>

<div class="portfolio">

  <div class="hero">
    <div class="hero-top">
      <div class="hero-badge">
        <span class="status-dot"></span> Open to opportunities
      </div>
      <div style="font-size:12px;color:#484f58;font-family:'JetBrains Mono',monospace;">
        Coimbatore, Tamil Nadu 📍
      </div>
    </div>

    <div class="hero-name">Manikandan <span>.</span></div>
    <div class="hero-role">
      <strong>Full Stack Developer & Team Lead</strong> — Building enterprise solutions that scale
    </div>

    <div class="hero-links">
      <div class="hero-link"><i class="ti ti-brand-github" aria-hidden="true"></i> Manikandan12155</div>
      <div class="hero-link"><i class="ti ti-world" aria-hidden="true"></i> manikandan-dev.netlify.app</div>
      <div class="hero-link"><i class="ti ti-mail" aria-hidden="true"></i> manianuram2312@gmail.com</div>
    </div>
  </div>

  <div class="section">
    <div class="section-label">// about me</div>
    <div class="code-block">
      <div class="code-top">
        <div class="dot dot-r"></div>
        <div class="dot dot-y"></div>
        <div class="dot dot-g"></div>
      </div>
      <div>
        <span class="kw">class</span> <span class="cn">Manikandan</span> <span class="op">{</span><br/>
        &nbsp;&nbsp;<span class="op">String</span> <span class="cn">name</span>      <span class="op">=</span> <span class="str">"Manikandan"</span><span class="op">;</span><br/>
        &nbsp;&nbsp;<span class="op">String</span> <span class="cn">location</span>  <span class="op">=</span> <span class="str">"Coimbatore, Tamil Nadu, India"</span><span class="op">;</span><br/>
        &nbsp;&nbsp;<span class="op">String</span> <span class="cn">role</span>      <span class="op">=</span> <span class="str">"Full Stack Developer &amp; Team Lead"</span><span class="op">;</span><br/>
        &nbsp;&nbsp;<span class="op">int</span>    <span class="cn">experience</span> <span class="op">=</span> <span class="num">3</span><span class="op">;</span> <span class="cm">// years</span><br/>
        <br/>
        &nbsp;&nbsp;<span class="op">String[]</span> <span class="cn">stack</span> <span class="op">= {</span> <span class="str">"React"</span><span class="op">,</span> <span class="str">"Angular"</span><span class="op">,</span> <span class="str">"Next.js"</span><span class="op">,</span> <span class="str">".NET Core"</span><span class="op">,</span> <span class="str">"FastAPI"</span> <span class="op">};</span><br/>
        <br/>
        &nbsp;&nbsp;<span class="fn">String</span> <span class="cn">motto</span><span class="op">() {</span><br/>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">return</span> <span class="str">"Build systems that scale, write code that lasts."</span><span class="op">;</span><br/>
        &nbsp;&nbsp;<span class="op">}</span><br/>
        <span class="op">}</span>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="section-label">// impact at a glance</div>
    <div class="stats-row">
      <div class="stat-card">
        <span class="stat-num">3+</span>
        <span class="stat-label">Years Exp</span>
      </div>
      <div class="stat-card">
        <span class="stat-num">10+</span>
        <span class="stat-label">Enterprise Projects</span>
      </div>
      <div class="stat-card">
        <span class="stat-num">3K+</span>
        <span class="stat-label">Vendors Managed</span>
      </div>
      <div class="stat-card">
        <span class="stat-num">6+</span>
        <span class="stat-label">Global Clients</span>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="section-label">// tech stack</div>

    <div class="cat-label">Frontend</div>
    <div class="tech-grid">
      <div class="tech-badge"><div class="tech-dot" style="background:#61dafb"></div>React.js</div>
      <div class="tech-badge"><div class="tech-dot" style="background:#dd0031"></div>Angular</div>
      <div class="tech-badge"><div class="tech-dot" style="background:#000"></div>Next.js</div>
      <div class="tech-badge"><div class="tech-dot" style="background:#61dafb"></div>React Native</div>
      <div class="tech-badge"><div class="tech-dot" style="background:#f7df1e"></div>JavaScript</div>
      <div class="tech-badge"><div class="tech-dot" style="background:#3178c6"></div>TypeScript</div>
      <div class="tech-badge"><div class="tech-dot" style="background:#06b6d4"></div>Tailwind CSS</div>
      <div class="tech-badge"><div class="tech-dot" style="background:#7952b3"></div>Bootstrap</div>
    </div>

    <div class="cat-label">Backend & Database</div>
    <div class="tech-grid">
      <div class="tech-badge"><div class="tech-dot" style="background:#512bd4"></div>.NET Core</div>
      <div class="tech-badge"><div class="tech-dot" style="background:#239120"></div>C#</div>
      <div class="tech-badge"><div class="tech-dot" style="background:#009688"></div>FastAPI</div>
      <div class="tech-badge"><div class="tech-dot" style="background:#cc2927"></div>SQL Server</div>
      <div class="tech-badge"><div class="tech-dot" style="background:#4169e1"></div>PostgreSQL</div>
      <div class="tech-badge"><div class="tech-dot" style="background:#ff6c37"></div>REST API</div>
    </div>

    <div class="cat-label">Tools</div>
    <div class="tech-grid">
      <div class="tech-badge"><div class="tech-dot" style="background:#f05032"></div>Git</div>
      <div class="tech-badge"><div class="tech-dot" style="background:#fc6d26"></div>GitLab</div>
      <div class="tech-badge"><div class="tech-dot" style="background:#5c2d91"></div>Visual Studio</div>
      <div class="tech-badge"><div class="tech-dot" style="background:#007acc"></div>VS Code</div>
    </div>
  </div>

  <div class="section">
    <div class="section-label">// experience</div>
    <div class="exp-cards">
      <div class="exp-card">
        <div class="exp-header">
          <div>
            <div class="exp-company">Aagnia Technologies</div>
            <div class="exp-role">Full Stack Developer Team Lead</div>
          </div>
          <div class="exp-date">Jun 2025 → Present</div>
        </div>
        <ul class="exp-points">
          <li>Leading enterprise web & mobile app development across cross-functional teams</li>
          <li>Driving AI integration, chatbot development & intelligent workflow automation</li>
          <li>Mentoring developers, conducting code reviews & defining architecture standards</li>
        </ul>
      </div>
      <div class="exp-card">
        <div class="exp-header">
          <div>
            <div class="exp-company">Agaram InfoTech</div>
            <div class="exp-role">Senior Software Engineer</div>
          </div>
          <div class="exp-date">Aug 2022 → Jul 2025</div>
        </div>
        <ul class="exp-points">
          <li>Built ERP & enterprise systems for Pfizer, Fujitec, Hyundai Transys & Goodyear</li>
          <li>Developed React/Angular frontends + ASP.NET Core REST APIs at scale</li>
          <li>Designed SQL Server databases with complex reporting & integration workflows</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="section-label">// featured projects</div>
    <div class="proj-grid">
      <div class="proj-card">
        <div class="proj-client">Pfizer</div>
        <div class="proj-name">Asset Management System</div>
        <div class="proj-desc">RFID, QR & Barcode-based asset lifecycle tracking. Reduced manual monitoring effort significantly through automation.</div>
        <div class="proj-tags">
          <span class="proj-tag">React</span>
          <span class="proj-tag">.NET Core</span>
          <span class="proj-tag">SQL Server</span>
          <span class="proj-tag">RFID</span>
        </div>
      </div>
      <div class="proj-card">
        <div class="proj-client">LS Automotive India</div>
        <div class="proj-name">Vendor & Supplier Plan</div>
        <div class="proj-desc">Production planning platform managing 3,000+ vendors & suppliers with shipment coordination.</div>
        <div class="proj-tags">
          <span class="proj-tag">React</span>
          <span class="proj-tag">FastAPI</span>
          <span class="proj-tag">PostgreSQL</span>
        </div>
      </div>
      <div class="proj-card">
        <div class="proj-client">Fujitec</div>
        <div class="proj-name">Performance Management</div>
        <div class="proj-desc">Employee appraisal platform with automated review workflows, notifications & analytics dashboards.</div>
        <div class="proj-tags">
          <span class="proj-tag">Angular</span>
          <span class="proj-tag">ASP.NET Core</span>
          <span class="proj-tag">SQL Server</span>
        </div>
      </div>
      <div class="proj-card">
        <div class="proj-client">Hyundai Transys</div>
        <div class="proj-name">Complaint Management</div>
        <div class="proj-desc">Cross-platform complaint tracking across desktop & mobile, improving resolution efficiency end-to-end.</div>
        <div class="proj-tags">
          <span class="proj-tag">React Native</span>
          <span class="proj-tag">.NET Core</span>
          <span class="proj-tag">PostgreSQL</span>
        </div>
      </div>
    </div>
  </div>

  <div class="footer">
    <span class="footer-text">manikandan © 2025 · full stack developer</span>
    <div class="footer-actions">
      <button class="btn" onclick="sendPrompt('Generate the full improved README.md with this enhanced professional design, including all 13 sections with the dark theme and premium styling.')">
        <i class="ti ti-file-code" aria-hidden="true"></i> Generate Full README ↗
      </button>
      <button class="btn" onclick="sendPrompt('Make this portfolio README even more impressive — add LeetCode stats widget, contribution snake animation, and a dynamic visitor map section.')">
        <i class="ti ti-sparkles" aria-hidden="true"></i> Upgrade More ↗
      </button>
    </div>
  </div>

</div>
