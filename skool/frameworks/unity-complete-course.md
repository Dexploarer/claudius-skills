# Framework Course: Unity Complete Game Development

## 🎮 Course Overview

Master Unity game development from beginner to advanced, covering 2D, 3D, mobile, VR/AR, and multiplayer games.

**Duration:** 12 weeks | **Projects:** 8 complete games | **Level:** Beginner to Advanced

---

## 📚 Course Curriculum

### Week 1-2: Unity Fundamentals

#### C# Essentials for Unity
```csharp
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    [Header("Movement")]
    [SerializeField] private float moveSpeed = 5f;
    [SerializeField] private float jumpForce = 10f;

    [Header("References")]
    [SerializeField] private Rigidbody2D rb;
    [SerializeField] private Transform groundCheck;
    [SerializeField] private LayerMask groundLayer;

    private bool isGrounded;
    private float horizontalInput;

    void Update()
    {
        // Input
        horizontalInput = Input.GetAxisRaw("Horizontal");

        // Jump
        if (Input.GetButtonDown("Jump") && isGrounded)
        {
            Jump();
        }

        // Ground check
        isGrounded = Physics2D.OverlapCircle(groundCheck.position, 0.2f, groundLayer);
    }

    void FixedUpdate()
    {
        // Movement
        rb.velocity = new Vector2(horizontalInput * moveSpeed, rb.velocity.y);
    }

    void Jump()
    {
        rb.velocity = new Vector2(rb.velocity.x, jumpForce);
    }
}
```

#### Scene Management
```csharp
using UnityEngine;
using UnityEngine.SceneManagement;
using System.Collections;

public class GameManager : MonoBehaviour
{
    public static GameManager Instance { get; private set; }

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
        }
        else
        {
            Destroy(gameObject);
        }
    }

    public void LoadScene(string sceneName)
    {
        StartCoroutine(LoadSceneAsync(sceneName));
    }

    IEnumerator LoadSceneAsync(string sceneName)
    {
        AsyncOperation operation = SceneManager.LoadSceneAsync(sceneName);

        while (!operation.isDone)
        {
            float progress = Mathf.Clamp01(operation.progress / 0.9f);
            // Update loading bar
            yield return null;
        }
    }
}
```

**Project 1:** 2D Platformer with collectibles and enemies

### Week 3-4: 2D Game Development

#### Sprite Animation
```csharp
public class AnimationController : MonoBehaviour
{
    private Animator animator;
    private Rigidbody2D rb;

    void Start()
    {
        animator = GetComponent<Animator>();
        rb = GetComponent<Rigidbody2D>();
    }

    void Update()
    {
        animator.SetFloat("Speed", Mathf.Abs(rb.velocity.x));
        animator.SetBool("IsGrounded", isGrounded);
        animator.SetFloat("VerticalSpeed", rb.velocity.y);
    }
}
```

#### Tilemap System
```csharp
using UnityEngine.Tilemaps;

public class LevelGenerator : MonoBehaviour
{
    [SerializeField] private Tilemap groundTilemap;
    [SerializeField] private TileBase[] groundTiles;

    public void GenerateLevel(int width, int height)
    {
        for (int x = 0; x < width; x++)
        {
            for (int y = 0; y < height; y++)
            {
                Vector3Int pos = new Vector3Int(x, y, 0);
                TileBase tile = groundTiles[Random.Range(0, groundTiles.Length)];
                groundTilemap.SetTile(pos, tile);
            }
        }
    }
}
```

**Project 2:** Top-down shooter with procedural levels

### Week 5-6: 3D Game Development

#### Character Controller
```csharp
public class ThirdPersonController : MonoBehaviour
{
    [Header("Movement")]
    [SerializeField] private float moveSpeed = 6f;
    [SerializeField] private float rotationSpeed = 10f;
    [SerializeField] private float gravity = -9.81f;

    [Header("Camera")]
    [SerializeField] private Transform cameraTransform;

    private CharacterController controller;
    private Vector3 velocity;

    void Start()
    {
        controller = GetComponent<CharacterController>();
    }

    void Update()
    {
        Move();
        ApplyGravity();
    }

    void Move()
    {
        float horizontal = Input.GetAxisRaw("Horizontal");
        float vertical = Input.GetAxisRaw("Vertical");

        Vector3 direction = new Vector3(horizontal, 0f, vertical).normalized;

        if (direction.magnitude >= 0.1f)
        {
            // Calculate movement direction relative to camera
            float targetAngle = Mathf.Atan2(direction.x, direction.z) * Mathf.Rad2Deg +
                                cameraTransform.eulerAngles.y;

            Vector3 moveDir = Quaternion.Euler(0f, targetAngle, 0f) * Vector3.forward;

            controller.Move(moveDir * moveSpeed * Time.deltaTime);

            // Rotate character
            float angle = Mathf.SmoothDampAngle(
                transform.eulerAngles.y,
                targetAngle,
                ref rotationVelocity,
                rotationSpeed * Time.deltaTime
            );

            transform.rotation = Quaternion.Euler(0f, angle, 0f);
        }
    }

    void ApplyGravity()
    {
        if (controller.isGrounded && velocity.y < 0)
        {
            velocity.y = -2f;
        }

        velocity.y += gravity * Time.deltaTime;
        controller.Move(velocity * Time.deltaTime);
    }
}
```

#### Camera System
```csharp
public class CameraFollow : MonoBehaviour
{
    [SerializeField] private Transform target;
    [SerializeField] private Vector3 offset = new Vector3(0, 5, -10);
    [SerializeField] private float smoothSpeed = 0.125f;

    void LateUpdate()
    {
        Vector3 desiredPosition = target.position + offset;
        Vector3 smoothedPosition = Vector3.Lerp(transform.position, desiredPosition, smoothSpeed);
        transform.position = smoothedPosition;

        transform.LookAt(target);
    }
}
```

**Project 3:** 3D adventure game with quests

### Week 7-8: Advanced Systems

#### Inventory System
```csharp
[System.Serializable]
public class Item
{
    public string itemName;
    public Sprite icon;
    public int maxStack;
}

public class InventorySystem : MonoBehaviour
{
    public static InventorySystem Instance { get; private set; }

    [SerializeField] private int inventorySize = 20;

    private Dictionary<Item, int> inventory = new Dictionary<Item, int>();

    public bool AddItem(Item item, int quantity = 1)
    {
        if (inventory.ContainsKey(item))
        {
            if (inventory[item] + quantity <= item.maxStack)
            {
                inventory[item] += quantity;
                return true;
            }
        }
        else
        {
            if (inventory.Count < inventorySize)
            {
                inventory.Add(item, quantity);
                return true;
            }
        }

        return false; // Inventory full
    }

    public bool RemoveItem(Item item, int quantity = 1)
    {
        if (inventory.ContainsKey(item))
        {
            inventory[item] -= quantity;

            if (inventory[item] <= 0)
            {
                inventory.Remove(item);
            }

            return true;
        }

        return false;
    }

    public int GetItemCount(Item item)
    {
        return inventory.ContainsKey(item) ? inventory[item] : 0;
    }
}
```

#### Quest System
```csharp
[System.Serializable]
public class Quest
{
    public string questName;
    public string description;
    public int requiredAmount;
    public int currentAmount;
    public bool isCompleted;

    public void UpdateProgress(int amount)
    {
        currentAmount += amount;

        if (currentAmount >= requiredAmount)
        {
            isCompleted = true;
        }
    }
}

public class QuestManager : MonoBehaviour
{
    public List<Quest> activeQuests = new List<Quest>();

    public void AddQuest(Quest quest)
    {
        activeQuests.Add(quest);
    }

    public void UpdateQuest(string questName, int progress)
    {
        Quest quest = activeQuests.Find(q => q.questName == questName);

        if (quest != null)
        {
            quest.UpdateProgress(progress);

            if (quest.isCompleted)
            {
                CompleteQuest(quest);
            }
        }
    }

    void CompleteQuest(Quest quest)
    {
        Debug.Log($"Quest completed: {quest.questName}");
        // Grant rewards
        activeQuests.Remove(quest);
    }
}
```

**Project 4:** RPG with inventory, quests, and dialogue

### Week 9: Mobile Development

#### Touch Controls
```csharp
public class TouchController : MonoBehaviour
{
    [SerializeField] private FloatingJoystick joystick;
    [SerializeField] private float moveSpeed = 5f;

    private Rigidbody2D rb;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }

    void FixedUpdate()
    {
        Vector2 movement = new Vector2(joystick.Horizontal, joystick.Vertical);
        rb.velocity = movement * moveSpeed;
    }
}
```

#### Performance Optimization
```csharp
public class PerformanceManager : MonoBehaviour
{
    void Start()
    {
        // Set target frame rate for mobile
        Application.targetFrameRate = 60;

        // Optimize quality settings
        QualitySettings.vSyncCount = 0;

        // Disable unnecessary features
        if (Application.isMobilePlatform)
        {
            QualitySettings.shadows = ShadowQuality.Disable;
            QualitySettings.SetQualityLevel(2); // Medium quality
        }
    }
}
```

**Project 5:** Hyper-casual mobile game

### Week 10: Multiplayer with Photon

#### Network Player
```csharp
using Photon.Pun;

public class NetworkPlayer : MonoBehaviourPun
{
    void Update()
    {
        if (photonView.IsMine)
        {
            HandleInput();
        }
    }

    void HandleInput()
    {
        float horizontal = Input.GetAxisRaw("Horizontal");
        float vertical = Input.GetAxisRaw("Vertical");

        Vector3 movement = new Vector3(horizontal, 0, vertical);
        transform.position += movement * moveSpeed * Time.deltaTime;
    }
}
```

#### Room Management
```csharp
using Photon.Pun;
using Photon.Realtime;

public class NetworkManager : MonoBehaviourPunCallbacks
{
    void Start()
    {
        PhotonNetwork.ConnectUsingSettings();
    }

    public override void OnConnectedToMaster()
    {
        PhotonNetwork.JoinLobby();
    }

    public override void OnJoinedLobby()
    {
        PhotonNetwork.JoinOrCreateRoom("GameRoom", new RoomOptions { MaxPlayers = 4 }, null);
    }

    public override void OnJoinedRoom()
    {
        PhotonNetwork.Instantiate("Player", Vector3.zero, Quaternion.identity);
    }
}
```

**Project 6:** Multiplayer battle arena

### Week 11: VR Development

#### VR Interaction
```csharp
using UnityEngine.XR.Interaction.Toolkit;

public class VRGrabbable : XRGrabInteractable
{
    protected override void OnSelectEntered(SelectEnterEventArgs args)
    {
        base.OnSelectEntered(args);
        // Haptic feedback
        args.interactorObject.transform.GetComponent<XRController>()?.SendHapticImpulse(0.5f, 0.1f);
    }

    protected override void OnSelectExited(SelectExitEventArgs args)
    {
        base.OnSelectExited(args);
    }
}
```

**Project 7:** VR escape room

### Week 12: Polish & Publishing

#### Audio Manager
```csharp
public class AudioManager : MonoBehaviour
{
    public static AudioManager Instance;

    [SerializeField] private AudioSource musicSource;
    [SerializeField] private AudioSource sfxSource;

    void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
        }
        else
        {
            Destroy(gameObject);
        }
    }

    public void PlaySFX(AudioClip clip)
    {
        sfxSource.PlayOneShot(clip);
    }

    public void PlayMusic(AudioClip clip)
    {
        musicSource.clip = clip;
        musicSource.Play();
    }
}
```

#### Build Settings
- iOS: Xcode project
- Android: APK/AAB
- WebGL: Compressed build
- PC: Standalone executable

**Final Project:** Complete polished game for portfolio

---

## 🎓 Learning Outcomes

- ✅ Proficient in C# and Unity API
- ✅ Built 8 complete games
- ✅ Mobile optimization
- ✅ Multiplayer networking
- ✅ VR development basics
- ✅ Published to app stores

---

## 📚 Resources

- Unity Learn Premium
- Unity Documentation
- Brackeys YouTube
- Code Monkey Tutorials

---

**Course Complete!** Portfolio-ready Unity developer.
