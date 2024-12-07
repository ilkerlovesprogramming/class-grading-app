// Chart configuration with hacker theme
const chartConfig = {
    plugins: {
        legend: {
            labels: {
                font: {
                    family: 'monospace'
                },
                color: '#4ade80' // text-green-400
            }
        }
    },
    scales: {
        x: {
            grid: {
                color: '#22c55e20' // text-green-600 with opacity
            },
            ticks: {
                color: '#4ade80',
                font: {
                    family: 'monospace'
                }
            }
        },
        y: {
            grid: {
                color: '#22c55e20'
            },
            ticks: {
                color: '#4ade80',
                font: {
                    family: 'monospace'
                }
            }
        }
    }
};

// Initialize charts with empty data
function initializeCharts() {
    // Grade Distribution
    const gradeCtx = document.getElementById('gradeDistribution').getContext('2d');
    window.gradeChart = new Chart(gradeCtx, {
        type: 'bar',
        data: {
            labels: ['A', 'B', 'C', 'D', 'F'],
            datasets: [{
                label: 'Grade Distribution',
                data: [0, 0, 0, 0, 0],
                backgroundColor: '#22c55e40',
                borderColor: '#22c55e',
                borderWidth: 1
            }]
        },
        options: {
            ...chartConfig,
            responsive: true
        }
    });

    // Performance Trend
    const trendCtx = document.getElementById('performanceTrend').getContext('2d');
    window.trendChart = new Chart(trendCtx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Performance Trend',
                data: [],
                borderColor: '#22c55e',
                tension: 0.1,
                fill: true,
                backgroundColor: '#22c55e20'
            }]
        },
        options: {
            ...chartConfig,
            responsive: true
        }
    });

    // Course Progress
    const progressCtx = document.getElementById('courseProgress').getContext('2d');
    window.progressChart = new Chart(progressCtx, {
        type: 'radar',
        data: {
            labels: [],
            datasets: [{
                label: 'Course Progress',
                data: [],
                borderColor: '#22c55e',
                backgroundColor: '#22c55e20',
                pointBackgroundColor: '#22c55e'
            }]
        },
        options: {
            ...chartConfig,
            scales: {
                r: {
                    grid: {
                        color: '#22c55e20'
                    },
                    pointLabels: {
                        color: '#4ade80',
                        font: {
                            family: 'monospace'
                        }
                    },
                    ticks: {
                        color: '#4ade80',
                        font: {
                            family: 'monospace'
                        }
                    }
                }
            }
        }
    });
}

// Update charts with student data
function updateCharts(studentData) {
    // Update grade distribution
    gradeChart.data.datasets[0].data = studentData.gradeDistribution;
    gradeChart.update();

    // Update performance trend
    trendChart.data.labels = studentData.performanceDates;
    trendChart.data.datasets[0].data = studentData.performanceScores;
    trendChart.update();

    // Update course progress
    progressChart.data.labels = studentData.courseNames;
    progressChart.data.datasets[0].data = studentData.courseProgress;
    progressChart.update();
}

// Initialize when document is ready
document.addEventListener('DOMContentLoaded', function() {
    initializeCharts();
    
    // Setup student selector
    const studentSelector = document.getElementById('studentSelector');
    studentSelector.addEventListener('change', function() {
        if (this.value) {
            fetchStudentData(this.value);
        }
    });

    // Fetch initial student list
    fetchStudents();
});

// Fetch students for dropdown
async function fetchStudents() {
    try {
        const response = await fetch('/api/students/');
        const data = await response.json();
        const selector = document.getElementById('studentSelector');
        
        data.forEach(student => {
            const option = document.createElement('option');
            option.value = student.id;
            option.textContent = student.name;
            selector.appendChild(option);
        });
    } catch (error) {
        console.error('Error fetching students:', error);
    }
}

// Fetch student data and update UI
async function fetchStudentData(studentId) {
    try {
        // Fetch various student data endpoints
        const [details, grades, ongoing, completed] = await Promise.all([
            fetch(`/api/student/${studentId}/details/`).then(r => r.json()),
            fetch(`/api/student/${studentId}/grades/`).then(r => r.json()),
            fetch(`/api/student/${studentId}/ongoing-courses/`).then(r => r.json()),
            fetch(`/api/student/${studentId}/completed-courses/`).then(r => r.json())
        ]);

        // Update summary cards
        document.getElementById('avgGrade').textContent = `${details.average_grade}%`;
        document.getElementById('completedCourses').textContent = completed.length;
        document.getElementById('ongoingCourses').textContent = ongoing.length;
        document.getElementById('perfIndex').textContent = calculatePerformanceIndex(grades);

        // Update charts
        updateCharts({
            gradeDistribution: calculateGradeDistribution(grades),
            performanceDates: grades.map(g => g.date),
            performanceScores: grades.map(g => g.score),
            courseNames: [...ongoing, ...completed].map(c => c.name),
            courseProgress: [...ongoing, ...completed].map(c => c.progress)
        });

        // Update course table
        updateCourseTable([...ongoing, ...completed]);
    } catch (error) {
        console.error('Error fetching student data:', error);
    }
}

// Helper function to calculate grade distribution
function calculateGradeDistribution(grades) {
    const distribution = [0, 0, 0, 0, 0]; // A, B, C, D, F
    grades.forEach(grade => {
        if (grade.score >= 90) distribution[0]++;
        else if (grade.score >= 80) distribution[1]++;
        else if (grade.score >= 70) distribution[2]++;
        else if (grade.score >= 60) distribution[3]++;
        else distribution[4]++;
    });
    return distribution;
}

// Helper function to calculate performance index
function calculatePerformanceIndex(grades) {
    if (!grades.length) return '--';
    const avg = grades.reduce((sum, g) => sum + g.score, 0) / grades.length;
    const trend = grades.length > 1 ? 
        (grades[grades.length - 1].score - grades[0].score) / grades.length : 0;
    return Math.round((avg + trend * 10) / 2);
}

// Update course table
function updateCourseTable(courses) {
    const tbody = document.getElementById('courseTableBody');
    tbody.innerHTML = '';

    courses.forEach(course => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td class="px-6 py-4 whitespace-nowrap font-mono text-green-400">${course.code}</td>
            <td class="px-6 py-4 whitespace-nowrap font-mono text-green-400">${course.name}</td>
            <td class="px-6 py-4 whitespace-nowrap font-mono text-green-400">${course.grade || '--'}</td>
            <td class="px-6 py-4 whitespace-nowrap">
                <span class="px-2 inline-flex text-xs leading-5 font-mono font-semibold rounded-full 
                    ${course.status === 'Completed' ? 'bg-green-900 text-green-300' : 'bg-gray-900 text-green-400'}">
                    ${course.status}
                </span>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
                <div class="w-full bg-gray-900 rounded-full h-2">
                    <div class="bg-green-500 h-2 rounded-full" style="width: ${course.progress}%"></div>
                </div>
            </td>
        `;
        tbody.appendChild(row);
    });
}