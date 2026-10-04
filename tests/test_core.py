from app.core import get_app_status


def test_get_app_status():
    result= get_app_status()
    
    assert result["application"] == "DataForge AI"
    assert result["status"] == "healthy"
    assert result["version"] == "0.1.0"
    
    
    
    